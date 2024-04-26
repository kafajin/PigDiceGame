"""High Score Module

This module contains a class to manage high scores for a game.

"""


class HighScore:
    """A class to manage high scores fora game."""
    def __init__(self, filename="high_score.txt"):
        """
        Intialize the HighScore object

        Args:
            filename (str, optional): The name of the file to store high scores. Default is "high_scores.txt".    
        """
        self.filename = filename
        self.high_scores = {}

    def load_high_scores(self):
        """Load high scores from the file."""
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    player, score = line.strip().split(":")
                    self.high_scores[player] = int(score)
        except FileNotFoundError:
            # if the file doesnt exist, create an empty high_scores dictionary
            self.high_scores = {}

    def save_high_scores(self):
        """Save the high scores to the file."""
        try:
            with open(self.filename, "w") as file:
                for player, score in self.high_scores.items():
                    file.write(f"{player}:{score}\n")
        except Exception as e:
            print(f"Error occurred while saving high scores: {e}")

    def update_high_scores(self, winner_name, winner_score):
        """
        Update high scores with the latest game result.

        Args:
            winner_name (str): The name of the winning player.
            winner_score (str): The score achieved by the winning player
        """
        if winner_name in self.high_scores:
            self.high_scores[winner_name] = max(
                self.high_scores[winner_name],
                winner_score
            )
        else:
            self.high_scores[winner_name] = winner_score

    def display_high_scores(self):
        """Display the high scores."""
        print("High Scores:")
        if self.high_scores:
            sorted_scores = sorted(
                self.high_scores.items(),
                key=lambda x: x[1],
                reverse=True
            )
            max_name_length = max(len(name) for name, _ in sorted_scores)
            for i, (player, score) in enumerate(sorted_scores, start=1):
                padding = max_name_length - len(player) + 2
                print(f"{i}. {player}{' ' * padding}: {score}")
        else:
            print("No high scores to display.")
