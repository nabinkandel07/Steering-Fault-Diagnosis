"""Synthetic steering sensor fault classification with nearest centroids."""

import csv
import json
import math
import random
import statistics
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
CLASSES = ("normal", "bias", "stuck", "noise")


def make_signal(label, rng, length=120):
    phase = rng.uniform(0, 2 * math.pi)
    clean = [18 * math.sin(2 * math.pi * i / length + phase) + 4 * math.sin(6 * math.pi * i / length) for i in range(length)]
    if label == "normal":
        return [x + rng.gauss(0, 0.45) for x in clean]
    if label == "bias":
        return [x + 7.5 + rng.gauss(0, 0.45) for x in clean]
    if label == "stuck":
        level = clean[length // 3]
        return clean[: length // 3] + [level + rng.gauss(0, 0.08) for _ in range(length - length // 3)]
    return [x + rng.gauss(0, 4.0) for x in clean]


def features(signal):
    diffs = [b - a for a, b in zip(signal, signal[1:])]
    return (statistics.mean(signal), statistics.pstdev(signal), statistics.pstdev(diffs), max(abs(x) for x in diffs))


def distance(a, b):
    scales = (8.0, 8.0, 3.0, 10.0)
    return sum(((x - y) / s) ** 2 for x, y, s in zip(a, b, scales))


def main():
    RESULTS.mkdir(exist_ok=True)
    rng = random.Random(42)
    samples = [(label, features(make_signal(label, rng))) for label in CLASSES for _ in range(100)]
    train = [s for i, s in enumerate(samples) if i % 5]
    test = [s for i, s in enumerate(samples) if not i % 5]
    centroids = {}
    for label in CLASSES:
        vectors = [vector for sample_label, vector in train if sample_label == label]
        centroids[label] = tuple(statistics.mean(values) for values in zip(*vectors))
    matrix = {actual: {predicted: 0 for predicted in CLASSES} for actual in CLASSES}
    for actual, vector in test:
        predicted = min(CLASSES, key=lambda label: distance(vector, centroids[label]))
        matrix[actual][predicted] += 1
    total = len(test)
    correct = sum(matrix[label][label] for label in CLASSES)
    recalls = {label: matrix[label][label] / sum(matrix[label].values()) for label in CLASSES}
    metrics = {"test_samples": total, "accuracy": correct / total, "recall_by_class": recalls, "data": "deterministic synthetic steering-angle signals"}
    with (RESULTS / "confusion_matrix.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["actual/predicted", *CLASSES])
        for actual in CLASSES:
            writer.writerow([actual, *(matrix[actual][predicted] for predicted in CLASSES)])
    (RESULTS / "metrics.json").write_text(json.dumps(metrics, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(metrics, indent=2))


if __name__ == "__main__":
    main()
