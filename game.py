from computer_intelligence import ComputerIntelligence
from highscore import HighScore


high_scores = HighScore()


class Game:
    """
    Represents a game of Pig Dice.

    Attributes:
        players (list): A list of players participating in the game.
        current_player_index (int): index of the current player in the players list.
        dice: the dice used in the game.
        high_scores: the high scores manager for the game.
        turn (int): the current turn number in the game.
    """

    def __init__(self, players, dice, high_scores):
        """
        Initialize the Game object.

        Args:
            players (list): A list of Player objects representing the players in the game.
            dice: The dice object used in the game.
            high_scores: The high scores manager for the game.
        """
        self.players = players
        self.current_player_index = 0
        self.dice = dice
        self.high_scores = high_scores
        self.turn = 0

    def add_player(self, player):
        """
        Add a player to the game.

        Args:
            player: The Player object to be added to the game.
        """
        self.players.append(player)

    def switch_player(self):
        """Switch to the next player in the game."""
        self.current_player_index = (
            self.current_player_index + 1) % len(self.players)

    def play(self):
        """Start and manages the game."""
        print("\nWelcome to Pig Dice Game!\n")
        for player in self.players:
            print(f"Player {player.name} joined the game.")

        while all(player.get_score() < 100 for player in self.players):
            print("\n------------------------------")

            current_player = self.players[self.current_player_index]

            if isinstance(current_player, ComputerIntelligence):
                print("Computer is playing...")
                scores = sum(player.get_score() for player in self.players)
                decision = current_player.take_turn(scores)
                if decision == "roll":
                    dice_roll = self.dice.roll_dice()
                    print(f"Computer rolled a {dice_roll}.")
                    current_player.add_score(dice_roll)
                    current_score = current_player.get_score()
                    print(f"Computer's current score: {current_score}")
                    if dice_roll == 1:
                        print("Computer rolled a 1.")
                        print("No points gained this turn.")
                        current_player.reset_score()
                else:
                    print("Computer chose to hold.")
            else:
                choice = current_player.take_turn(self.dice)
                if choice == 'roll':
                    dice_roll = self.dice.roll_dice()
                    print(f"{current_player.name} rolled a {dice_roll}.")
                    if dice_roll == 1:
                        print("A 1 is rolled. No points gained this turn.")
                        current_player.reset_score()
                    else:
                        print(f"{current_player.name} chose to roll again.")
                        current_player.add_score(dice_roll)
                        current_score = current_player.get_score()
                        print(f"Your current score: {current_score}")
                elif choice == 'hold':
                    print(f"{current_player.name} chose to hold.")
                    self.switch_player()

            self.switch_player()
            self.turn += 1

        winner = max(self.players, key=lambda player: player.get_score())

        self.high_scores.update_high_scores(winner.name, winner.get_score())
        print("Updated highscors:", self.high_scores.high_scores)

        self.high_scores.save_high_scores()
