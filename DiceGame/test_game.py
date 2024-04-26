import unittest
from game import Game
from player import Player
from dice import Dice
from highscore import HighScore

class TestGame(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("Player1")
        self.player2 = Player("Player2")
        self.dice = Dice()
        self.high_scores = HighScore()
        self.game = Game([self.player1, self.player2], self.dice, self.high_scores)

    def test_add_player(self):
        initial_player_count = len(self.game.players)
        self.game.add_player(Player("Player3"))
        self.assertEqual(len(self.game.players), initial_player_count + 1)

    def test_switch_player(self):
        self.assertEqual(self.game.current_player_index, 0)
        self.game.switch_player()
        self.assertEqual(self.game.current_player_index, 1)
        self.game.switch_player()
        self.assertEqual(self.game.current_player_index, 0)

    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
