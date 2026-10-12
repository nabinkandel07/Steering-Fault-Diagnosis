# Results and interpretation

The held-out set contains 80 balanced windows. Overall accuracy is **86.25%** and macro F1 is **84.48%**.

| Class | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| Normal | 0.800 | 1.000 | 0.889 | 20 |
| Bias | 0.769 | 1.000 | 0.870 | 20 |
| Stuck | 1.000 | 0.450 | 0.621 | 20 |
| Noise | 1.000 | 1.000 | 1.000 | 20 |

![Confusion matrix](../results/confusion_matrix.svg)

Stuck faults have high precision but low recall: when the classifier predicts stuck it is correct, but 11 of 20 stuck windows are assigned to another class. The result identifies a concrete research direction—add temporal plateau duration, derivative sparsity, and change-point features rather than presenting accuracy alone.

These values describe the deterministic synthetic benchmark only. `results/classification_report.csv` and `results/confusion_matrix.csv` provide machine-readable evidence.
