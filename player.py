import sys


class Player:
    """Class representing a player in the Pig Dice Game.

    Attributes:
        name (str): The name of the player.
        score (int): The current score of the player.
    """

    def __init__(self, name):
        """Initialize a player with a given name and a starting score of 0."""
        self.name = name
        self.score = 0

    def reset_score(self):
        """Reset the player's score to 0."""
        self.score = 0

    def add_score(self, points):
        """Add points to the player's score.

        Args:
            points (int): The points to add to the player's score.
        """
        self.score += points

    def get_score(self):
        """Get the player's current score.

        Returns:
            int: The player's current score.
        """
        return self.score

    def take_turn(self, dice):
        """Simulate the player's turn in the game.

        Args:
            dice (Dice): The instance of the Dice class used in the game.

        Returns:
            bool: False if the player's turn is over, True otherwise.
        """
        print(f"It's {self.name}'s turn.")

        roll = input("Roll, hold, quit or cheat? (r/h/q/c): ").lower()
        if roll == 'r':
            dice_roll = dice.roll_dice()
            print(f"{self.name} rolled a {dice_roll}.")
            if dice_roll == 1:
                print("A 1 is rolled. No points gained this turn.")
                self.reset_score()
                return False

            else:
                self.add_score(dice_roll)
                print(f"Your current score: {self.get_score()}")
        elif roll == 'h':
            print(f"{self.name} chose to hold.")
            return False
        elif roll == 'q':
            print("Quiting the game. Thanks for playing")
            sys.exit()
        elif roll == 'c':
            print("Cheat code activated...")
            self.score = 100
            
            return False
        else:
            print("Invalid input. Please enter 'r' to roll or 'h' to hold or 'q' to quit.")

    def select_name(self):
        """Prompt the player to enter their name."""
        human_name = input("\nPlease enter your name: ")
        if not human_name:
            print("Name cannot be empty ")
        else:
            self.name = human_name
            print(f"Player's name set to {human_name}.")

    def change_name(self, new_playername):
        """Change the player's name to a new name.

        Args:
            new_playername (str): The new name for the player.

        Raises:
            ValueError: If the new name is empty.
        """
        if not new_playername:
            raise ValueError("Name cannot be empty. Please enter a name.")
        else:
            old_name = self.name
            self.name = new_playername
            print(f"Player's name changed from {old_name} to {new_playername}")

    def hold(self):
        """End the player's turn and add the round score to the player's total score."""
        self.round_score = 0
        self.score += self.round_score
