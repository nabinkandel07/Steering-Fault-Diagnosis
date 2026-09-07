# Steering Fault Diagnosis

A dependency-free Python baseline for classifying steering-angle sensor signals as `normal`, `bias`, `stuck`, or `noise`. It generates deterministic synthetic signals, extracts four statistical features, trains class centroids, and evaluates a nearest-centroid classifier on a held-out split.

## Run

```bash
python src/run_demo.py
```

Python 3.10 or newer is recommended. No third-party packages are required.

## Reproducible demo result

| Metric | Result |
|---|---:|
| Held-out samples | 80 |
| Overall accuracy | 86.25% |
| Normal recall | 100% |
| Bias recall | 100% |
| Stuck recall | 45% |
| Noise recall | 100% |

The weaker stuck-fault recall exposes the limit of this small feature set. All signals are synthetic, so these numbers are a reproducible pipeline check rather than evidence of performance on a vehicle.

Generated artifacts are committed under `results/`: `metrics.json` and `confusion_matrix.csv`.

## Method

Features include signal mean, signal standard deviation, first-difference standard deviation, and maximum step change. Classification uses normalized Euclidean distance to class centroids fitted on the training partition.

## Next steps

Validate on timestamped steering sensor logs, add windowed temporal features, compare tree and sequence models, and report performance across vehicles and operating conditions.
