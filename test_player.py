import unittest
from unittest.mock import patch
import sys
from player import Player
from dice import Dice  # Import Dice class if you have it

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("")  # Initialize player's name to empty string
        self.dice = Dice()  # Create a Dice object

    def test_reset_score(self):
        self.player.score = 50
        self.player.reset_score()
        self.assertEqual(self.player.score, 0)

    def test_add_score(self):
        self.player.add_score(50)
        self.assertEqual(self.player.score, 50)
        self.player.add_score(100)
        self.assertEqual(self.player.score, 150)

    def test_get_score(self):
        self.assertEqual(self.player.get_score(), 0)
        self.player.score = 100
        self.assertEqual(self.player.get_score(), 100)



    @patch('builtins.input', side_effect=['invalid', 'h'])
    @patch('sys.exit')
    def test_take_turn_invalid_then_hold(self, mock_exit, mock_input):
        self.player.take_turn(self.dice)  # Pass the dice object
        mock_exit.assert_not_called()  # sys.exit() should not be called for invalid input
        self.assertFalse(self.player.take_turn(self.dice))  # Should return False after holding

    @patch('builtins.input', return_value='NewName')
    def test_change_name(self, mock_input):
        self.player.change_name('NewName')
        self.assertEqual(self.player.name, 'NewName')

if __name__ == '__main__':
    unittest.main()
