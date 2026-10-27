"""r1.13 recorder (cp -n of postmortem_20261026/pm_record.py; only change: the 67150 guard, DV-R266). Post-mortem recorder: the frozen r1.10b RGB recorder loop (RD.record_rgb) re-stated step for step in this file (the
frozen file is imported, never edited; RD.rgb_format_window / RD.check_frame / DM.executed_action / DM.enemy_box /
SP.policy reused), with extra report-only columns per step:
  figs        = env.scene['figs'] (DoomPlayer labels other than self, the sealed interp1 _scene count)
  ally_vis    = env.scene['ally_visible']; n_seen = number of bound enemies label-visible
  fig_boxes   = up to 4 (x,y,w,h) of those DoomPlayer labels (padded -1)
--no-frames: no frames saved (used for replays of already-recorded scoring seeds, whose stored columns are compared).
Same seed -> same env, same eps rng (default_rng(seed)) -> same trajectory as the original recording (checked)."""
import argparse, json, math, os, time
from pathlib import Path
import numpy as np
import sys; sys.path.insert(0, "/Users/dude/rgl-proofs/GO-RGL-INTERP-1/scratch/rung_r3p5/postmortem_20261026")   # r1.13: pm_common lives there
import pm_common as PC
import r18_core as K
import r18_demos as DM
import r110_demo_rgb as RD

ap = argparse.ArgumentParser()
ap.add_argument("--seed", type=int, required=True)
ap.add_argument("--steps", type=int, default=20000)
ap.add_argument("--out", required=True)
ap.add_argument("--no-frames", action="store_true")
a = ap.parse_args()
seed = int(a.seed)
assert seed not in K.REAL
if seed in PC.RESERVED:                      # r1.13 DV-R266: 67150 only inside the sealed, FROZEN-gated scoring
    import sys as _s; _s.path.insert(0, str(Path(__file__).resolve().parent)); import r113_common as RC
    _why = RC.frozen_refusals() + ([] if os.environ.get("R113_SEALED_SCORE") == "1" else ["not the sealed scoring"])
    _why += [] if (RC.REAL_ROOT / "score" / RC.SEAL_MARK).is_file() else ["no seal marker"]
    if seed != RC.TEST_SEED or _why:
        raise SystemExit(f"refused: recording {seed}: {_why}")
out = Path(a.out); out.mkdir(parents=True, exist_ok=False)
cwd = os.getcwd(); os.chdir(out)
import scripted_kd05_copy as SP
from interp1 import envs as E
from diag import envr3p5 as EV
E.set_settle_log(out / E.SETTLE_LOG_NAME)
with RD.rgb_format_window(EV):
    env = EV.EnvB35(seed, K.CAND, screen=(60, 80), reward="d9_hits")
E._b1()
from rglv3.vz.glue import MATCH_TOL
rng = np.random.default_rng(seed)
EXTRA = ("figs", "ally_vis", "n_seen", "fig_boxes")
keys = [k for k in DM.FIELDS if k != "obs_next_strided"] + list(EXTRA)
buf = {k: [] for k in keys}
n_chunk, ep, t, t0, files = 0, 0, 0, time.time(), []
tot = {"steps": 0, "episodes": 0, "kills": 0.0, "hits": 0, "noise_steps": 0}

def flush():
    global n_chunk
    if not buf["label"]:
        return
    arrs = {k: np.asarray(v) for k, v in buf.items() if k != "frames"}
    p = out / f"demo_{seed}_{n_chunk:03d}.npz"
    with open(p, "xb") as f: np.savez(f, **arrs)
    if not a.no_frames:
        with open(out / f"demo_{seed}_{n_chunk:03d}_frames.npy", "xb") as f:
            np.save(f, np.asarray(buf["frames"], dtype=np.uint8))
    files.append(p.name); n_chunk += 1
    for k in buf: buf[k].clear()

try:
    env.reset()
    for _i in range(int(a.steps)):
        st = env.g.get_state()
        frame = np.zeros(RD.RGB_SHAPE, np.uint8) if st is None else RD.check_frame(st.screen_buffer)
        gv, seen = dict(env.gvd), list(env.scene.get("seen_slots") or [])
        sc = env.scene
        label, _v = SP.policy(env, False)
        executed, noise = DM.executed_action(rng, label, K.DEMO_EPS)
        err = K.nearest_visible_err(gv, seen)
        box = DM.enemy_box(st, gv, seen, MATCH_TOL)
        fb = []
        if st is not None:
            sx, sy = sc["pos"]
            for lab in st.labels:
                if str(lab.object_name) == "DoomPlayer" and math.hypot(lab.object_position_x - sx, lab.object_position_y - sy) >= 1.0:
                    fb.append((int(lab.x), int(lab.y), int(lab.width), int(lab.height)))
        fb = (fb + [(-1, -1, -1, -1)] * 4)[:4]
        figs, ally_vis, n_seen = int(sc.get("figs") or 0), bool(sc.get("ally_visible")), len(seen)
        _obs, _r, done, row = env.step(executed)
        if not a.no_frames: buf["frames"].append(frame)
        buf["scalars"].append(K.scalars(gv)); buf["label"].append(int(label))
        buf["executed"].append(executed); buf["vis"].append(K.visible(seen))
        buf["err"].append(np.nan if err is None else float(err)); buf["box"].append(box)
        buf["episode"].append(ep); buf["t"].append(t); buf["kills"].append(float(row["kills"]))
        buf["hits"].append(int(row.get("enemy_hits") or 0)); buf["ep_start"].append(t == 0)
        buf["noise"].append(noise)
        buf["row_enemy_visible"].append(bool(row["enemy_visible"])); buf["row_shot"].append(bool(row["shot"]))
        buf["next_same_episode"].append(not done)
        buf["figs"].append(figs); buf["ally_vis"].append(ally_vis); buf["n_seen"].append(n_seen); buf["fig_boxes"].append(fb)
        tot["steps"] += 1; tot["kills"] += float(row["kills"]); tot["hits"] += int(row.get("enemy_hits") or 0)
        tot["noise_steps"] += int(noise)
        t += 1
        if done:
            ep, t = ep + 1, 0; tot["episodes"] += 1; env.reset()
        if len(buf["label"]) >= DM.CHUNK:
            flush()
    flush()
finally:
    env.close()
tot.update(seed=seed, eps=K.DEMO_EPS, check=False, wall_s=round(time.time() - t0, 1), files=files, chunk=DM.CHUNK,
           screen_format="RGB24" if not a.no_frames else "NONE(replay)", frame_shape=list(RD.RGB_SHAPE),
           extra_columns=list(EXTRA), recorder="r113/r113_record.py (= pm_record.py loop)",
           scripted_source_sha256=PC.sha(PC.C_DIR / "r1_8" / "scripted_kd05_copy.py"))
with open(out / "DEMO_SUMMARY.json", "x") as f:
    f.write(json.dumps(tot, indent=1, sort_keys=True) + "\n")
os.chdir(cwd)
print(json.dumps({k: v for k, v in tot.items() if k != "files"}))
