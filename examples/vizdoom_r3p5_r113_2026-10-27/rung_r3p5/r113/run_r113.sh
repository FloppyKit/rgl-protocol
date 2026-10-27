#!/bin/bash
# r1.13 P0-SEEDS launcher. Usage:  run_r113.sh smoke <TAG>   |   run_r113.sh real
# real is refused by r113_run.py unless Verify's FROZEN_r1.13.json is present and valid. CPU only. Never deletes.
set -u
PY=/Volumes/MiniHangar/rgl-envs/GO-RGL-INTERP-1.venv/bin/python
H=/Users/dude/rgl-proofs/GO-RGL-INTERP-1/scratch/rung_r3p5/r113
export OMP_NUM_THREADS=3 MKL_NUM_THREADS=3 PYTHONDONTWRITEBYTECODE=1
case "${1:-}" in
  smoke) [ -n "${2:-}" ] || { echo "usage: run_r113.sh smoke TAG"; exit 64; }; exec $PY -B $H/r113_run.py --smoke "$2" ;;
  real)  exec $PY -B $H/r113_run.py --real ;;
  *) echo "usage: run_r113.sh smoke TAG | real"; exit 64 ;;
esac
