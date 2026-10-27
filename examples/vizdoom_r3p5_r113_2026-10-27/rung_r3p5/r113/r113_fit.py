"""r1.13 one fit (spec §1-§4): the unchanged T1 recipe on the pre-registered training seeds, early-stopped on the val
seed with the predeclared rule, chosen checkpoint by the frozen select_epoch rule. Writes <root>/fits/<fit>/:
model_chosen.pt, RESULT.json (+ report-only scores on used seeds 67149/67148/67146 in real mode).
Never reads, records or scores 67150. Usage (via r113_run.py only):
  r113_fit.py --root DIR --fit A|B|C [--smoke --steps-cap N --eval-every N --min-steps N --patience N --val-limit N]"""
import argparse, copy, json, os, sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import r113_common as RC  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument("--root", required=True)
ap.add_argument("--fit", required=True, choices=sorted(RC.INIT_SEEDS))
ap.add_argument("--smoke", action="store_true")
ap.add_argument("--steps-cap", type=int, default=RC.MAX_STEPS)
ap.add_argument("--eval-every", type=int, default=RC.EVAL_EVERY)
ap.add_argument("--min-steps", type=int, default=RC.MIN_STEPS)
ap.add_argument("--patience", type=int, default=RC.PATIENCE)
ap.add_argument("--val-limit", type=int, default=0)
a = ap.parse_args()

if not a.smoke and (a.steps_cap, a.eval_every, a.min_steps, a.patience, a.val_limit) != (
        RC.MAX_STEPS, RC.EVAL_EVERY, RC.MIN_STEPS, RC.PATIENCE, 0):
    sys.exit("refused: real fits use the pre-registered early-stopping constants only")
train = list(RC.SMOKE_TRAIN if a.smoke else RC.TRAIN_SEEDS)
val = RC.SMOKE_VAL if a.smoke else RC.VAL_SEED
why = RC.seed_list_refusals(train, val, RC.SMOKE_TEST_SEED if a.smoke else RC.TEST_SEED, smoke=a.smoke)
if why:
    sys.exit(f"refused: {why}")
os.environ.setdefault("OMP_NUM_THREADS", str(RC.THREADS_PER_FIT))
import numpy as np, torch, torch.nn as nn  # noqa: E402
import r19b_p0 as P9  # noqa: E402
import r111_p0 as P  # noqa: E402
torch.set_num_threads(RC.THREADS_PER_FIT)

out = Path(a.root) / "fits" / a.fit
out.mkdir(parents=True, exist_ok=False)
init_seed = RC.INIT_SEEDS[a.fit]
t0 = time.time()
tr = RC.Multi({s: RC.demo_dir(s) for s in train})
va = RC.Multi({val: RC.demo_dir(val)}, limit=a.val_limit or None)
lab = tr.lab
all_idx = np.arange(len(tr)); vis_idx = all_idx[lab["vis"]]
torch.manual_seed(init_seed); rng = np.random.default_rng(init_seed); mrng = P.mirror_rng(init_seed)
net = P9.ProbeNet2((120, 160), 3)
opt = torch.optim.Adam(net.parameters(), lr=P.LR)
bce = nn.BCEWithLogitsLoss(reduction="none")
sampler = P9.HalfVisibleSampler(vis_idx, all_idx, rng, batch=P.BATCH, half=P.HALF_VIS)
info = {"train_frames": int(len(tr)), "train_visible": int(lab["vis"].sum()), "val_frames": int(len(va)),
        "val_visible": int(va.lab["vis"].sum())}
print(json.dumps({"fit": a.fit, "init_seed": init_seed, "smoke": a.smoke, **info}), flush=True)
hist, best, es, stop_reason, step = [], None, {}, None, 0
while stop_reason is None:
    step += 1
    ix = sampler.next()
    flip = mrng.random(len(ix)) < P.MIRROR_P
    vis = lab["vis"][ix]
    x = RC.x_of(tr, ix, flip)
    yl = torch.as_tensor(P.mirror_left(lab["left"][ix], tr.err[ix], vis, flip).astype(np.float32))
    w = P.lr_weight(tr.box[ix], vis, flip)
    yv = torch.as_tensor(vis.astype(np.float32)); yc = torch.as_tensor(lab["cen"][ix].astype(np.float32))
    ov, ol, oc = net(x)
    loss = bce(ov, yv).mean() + bce(oc, yc).mean()
    mk = (yv > 0) & torch.as_tensor(w > 0)
    if mk.any():
        loss = loss + bce(ol[mk], yl[mk]).mean()
    opt.zero_grad(); loss.backward(); opt.step()
    if step % a.eval_every == 0:
        vm, _ = RC.metrics(net, va)
        h = {"epoch": len(hist), "step": step, "val": {k: vm[k] for k in ("visible_auc", "lr_acc", "centred_auc", "n_visible")},
             "wall_s": round(time.time() - t0, 1), "loss": float(loss.detach())}
        h["improved"] = RC.es_update(es, h)
        hist.append(h)
        if P9.select_epoch(hist) == h["epoch"]:
            best = copy.deepcopy(net.state_dict())
        h["since"] = es["since"]
        print(json.dumps(h), flush=True)
        stop_reason = RC.es_should_stop(es, step, a.min_steps, a.steps_cap, a.patience)
    elif step >= a.steps_cap:
        stop_reason = "max_steps_no_eval"
chosen = P9.select_epoch(hist) if hist else None
if best is None:
    best = copy.deepcopy(net.state_dict())
with open(out / "model_chosen.pt", "xb") as f:
    torch.save(best, f)
res = {"fit": a.fit, "init_seed": init_seed, "smoke": a.smoke, "train_seeds": train, "val_seed": val,
       "eval_every": a.eval_every, "min_steps": a.min_steps, "max_steps": a.steps_cap, "patience": a.patience,
       "min_delta": RC.MIN_DELTA, "stop_step": step, "stop_reason": stop_reason, "chosen_eval": chosen,
       "chosen_step": hist[chosen]["step"] if hist else None,
       "val_auc_chosen": hist[chosen]["val"]["visible_auc"] if hist else None,
       "val_lr_chosen": hist[chosen]["val"]["lr_acc"] if hist else None,
       "val_history": hist, **info, "model_sha256": RC.sha(out / "model_chosen.pt"),
       "recipe": "r111c T1 unchanged (ProbeNet2 RGB 120x160, Adam 1e-3, batch 64 = 32 vis + 32 any, mirror p0.5 + "
                 "label swap + 1px mask, BCE vis+cen+LR); r1.13 early stopping", "report_scores": {}}
net.load_state_dict(best)
if not a.smoke:                                                    # report-only, used seeds, never 67150
    for s in RC.REPORT_SEEDS:
        sc = RC.Multi({s: RC.demo_dir(s)})
        m, (pv, pl, pc) = RC.metrics(net, sc)
        off, n_off = RC.lr_offcentre(pl, sc)
        res["report_scores"][str(s)] = {"visible_auc": m["visible_auc"], "lr_acc": m["lr_acc"], "n_visible": m["n_visible"],
                                        "lr_small": m["by_box"]["small"]["lr_acc"], "lr_large": m["by_box"]["large"]["lr_acc"],
                                        "lr_offcentre9": off, "n_offcentre9": n_off}
        print("report", s, round(m["visible_auc"], 4), round(m["lr_acc"], 4), flush=True)
res["wall_s"] = round(time.time() - t0, 1)
RC.jw(out / "RESULT.json", res)
print("DONE", a.fit, stop_reason, step, res["wall_s"], flush=True)
