"""Post-mortem 2026-10-26 (report-only, quick experiment). Shared paths/imports. Never edits frozen code; never deletes."""
from __future__ import annotations
import os, sys, json, hashlib
from pathlib import Path
C_DIR = Path("/Users/dude/rgl-proofs/GO-RGL-INTERP-1/scratch/rung_r3p5")
HERE = Path(__file__).resolve().parent
os.environ.setdefault("R110_C_DIR", str(C_DIR)); os.environ.setdefault("R111_C_DIR", str(C_DIR))
for _p in (str(C_DIR), str(C_DIR / "r1_8"), str(C_DIR / "r1_9b"), str(C_DIR / "r1_10b"), str(C_DIR / "r1_12"), str(HERE)):
    if _p not in sys.path:
        sys.path.insert(0, _p)
RUNS = Path("/Volumes/MiniHangar/rgl-artifacts/GO-RGL-INTERP-1/rung_r3p5_runs")
OUT = RUNS / "postmortem_20261026"
RESERVED = (67150,)          # never touched
def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""): h.update(b)
    return h.hexdigest()
def jw(p, obj):
    with open(p, "x") as f: f.write(json.dumps(obj, indent=1, sort_keys=True, default=float) + "\n")
