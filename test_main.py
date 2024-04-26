import unittest
from unittest.mock import patch
from game import Game
from player import Player
from computer_intelligence import ComputerIntelligence
from dice import Dice
from highscore import HighScore


class TestGame(unittest.TestCase):
    def test_add_player(self):
        player1 = Player("Player 1")
        player2 = Player("Player 2")
        players = [player1]
        game = Game(players, Dice(), HighScore())

        self.assertEqual(len(game.players), 1)  # Initially, there's only one player
        game.add_player(player2)
        self.assertEqual(len(game.players), 2)  # After adding another player, there should be two


    @patch('builtins.input', side_effect=["r", "c"])
    def test_play_cheat_code(self, mock_input):
        # Test for a scenario where the player rolls then uses the cheat code
        player1 = Player("Player 1")
        player2 = ComputerIntelligence()
        game = Game([player1, player2], Dice(), HighScore())

        game.play()
        # Ensure that the current player's score is 100 after using the cheat code
        self.assertEqual(player1.get_score(), 100)


if __name__ == '__main__':
    unittest.main()
