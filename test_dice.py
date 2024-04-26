import unittest
from dice import Dice

class TestDice(unittest.TestCase):
    def test_roll_dice(self):
        for _ in range(10):
            rolled_value = Dice.roll_dice()
            self.assertIn(rolled_value, range(1, 7))  # Ensure the rolled value is between 1 and 6

    def test_show_dice(self):
        for i in range(1, 7):
            dice_art = Dice.show_dice(i)
            self.assertIsInstance(dice_art, tuple)  # Ensure the output is a tuple
            self.assertEqual(len(dice_art), 5)  # Ensure there are 5 lines for each dice face

if __name__ == '__main__':
    unittest.main()
