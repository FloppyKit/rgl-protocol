#!/bin/bash
# r1.13 (DV-R262): record 5 fresh RGB demo seeds 67190-67194 for TRAINING ONLY (20,000 steps each, eps 0.1, KD05),
# with the unchanged post-mortem recorder (postmortem_20261026/pm_record.py, the frozen RD.record_rgb loop). 3 lanes.
# Never records 67150. Never deletes. Output dirs are created by pm_record (exist_ok=False: no overwrite).
set -u
PY=/Volumes/MiniHangar/rgl-envs/GO-RGL-INTERP-1.venv/bin/python
O=/Volumes/MiniHangar/rgl-artifacts/GO-RGL-INTERP-1/rung_r3p5_runs/r113_demos
cd /Users/dude/rgl-proofs/GO-RGL-INTERP-1/scratch/rung_r3p5/postmortem_20261026
mkdir -p $O/demos_rgb $O/logs
lane() { for s in "$@"; do
  [ "$s" = "67150" ] && { echo "refused 67150" >> $O/logs/rec_lanes.log; continue; }
  $PY -B pm_record.py --seed $s --steps 20000 --out $O/demos_rgb/demo_rgb_$s > $O/logs/rec_$s.log 2>&1
  echo "$(date '+%F %T %Z') $s rc=$?" >> $O/logs/rec_lanes.log; done; }
lane 67190 67193 &
lane 67191 67194 &
lane 67192 &
wait
echo "$(date '+%F %T %Z') ALL_DONE" >> $O/logs/rec_lanes.log
