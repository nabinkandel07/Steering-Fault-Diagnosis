# Data dictionary

The raw synthetic windows are generated at runtime and are not committed. This avoids presenting generated signals as measured vehicle data.

## Classes

| Label | Injection |
|---|---|
| `normal` | Nominal steering waveform plus low measurement noise |
| `bias` | Nominal waveform plus a constant positive offset |
| `stuck` | Signal freezes after one-third of the window |
| `noise` | Nominal waveform plus high-amplitude Gaussian noise |

## Result files

`confusion_matrix.csv` uses actual classes as rows and predicted classes as columns. `classification_report.csv` contains `class`, `precision`, `recall`, `f1`, and `support`. `metrics.json` contains overall accuracy, macro F1, class recall, sample count, and the synthetic-data declaration.
