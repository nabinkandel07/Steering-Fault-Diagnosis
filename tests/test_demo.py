import random
import unittest

from src.run_demo import CLASSES, features, make_signal


class SteeringFeatureTests(unittest.TestCase):
    def test_features_are_finite_and_complete(self):
        vector = features(make_signal("normal", random.Random(1)))
        self.assertEqual(len(vector), 4)
        self.assertTrue(all(abs(value) < 1000 for value in vector))

    def test_all_fault_generators_return_equal_windows(self):
        lengths = {len(make_signal(label, random.Random(2))) for label in CLASSES}
        self.assertEqual(lengths, {120})


if __name__ == "__main__":
    unittest.main()
