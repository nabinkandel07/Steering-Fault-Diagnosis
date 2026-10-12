# Methodology

## Research question

Can a small, interpretable feature set distinguish common steering-angle sensor fault patterns in fixed-length windows?

## Synthetic dataset

The deterministic generator uses seed 42 and creates 100 windows for each of four balanced classes: normal, additive bias, stuck sensor, and high noise. Every window has 120 samples. The nominal motion combines one fundamental sinusoid with a smaller third-harmonic term and random phase.

Faults are injected as a `+7.5` offset, a signal frozen after one-third of the window, or Gaussian noise with standard deviation `4.0`. Normal and bias cases include Gaussian measurement noise with standard deviation `0.45`.

## Features and classifier

Four interpretable features are extracted: signal mean, signal standard deviation, first-difference standard deviation, and maximum absolute step. The deterministic split assigns 320 windows to training and 80 to testing, preserving 20 test windows per class. Classification uses normalized squared Euclidean distance to each training-class centroid.

## Evaluation

The script reports confusion counts, accuracy, per-class precision, recall, F1, and macro F1. The test partition is held out from centroid estimation.

## Limitations

Synthetic fault shapes do not represent the full range of steering systems, driving maneuvers, sampling rates, temperature effects, or compound faults. Vehicle-level validation must group splits by vehicle or drive to avoid correlated-window leakage.
