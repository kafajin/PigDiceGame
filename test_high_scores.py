import io
import unittest
import os
from unittest import mock  # Import mock from unittest

from highscore import HighScore

class TestHighScore(unittest.TestCase):
    def setUp(self):
        self.filename = "test_high_scores.txt"
        self.high_score = HighScore(self.filename)

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)


    def test_load_and_save_high_scores(self):
        # Prepare test data
        self.high_score.high_scores = {"Player4": 300, "Player5": 250, "Player6": 200}

        # Test if high scores can be saved to file and then loaded
        self.high_score.save_high_scores()
        new_high_score = HighScore(self.filename)
        new_high_score.load_high_scores()

        self.assertEqual(new_high_score.high_scores, {"Player4": 300, "Player5": 250, "Player6": 200})


if __name__ == '__main__':
    unittest.main()
