from random import choice
from player import Player


class ComputerIntelligence(Player):
    """
    Represents a computer player with different levels of intelligence.

    Attributes:
        difficulty (str): The difficulty level of the computer intelligence.
    """
    def __init__(self, difficulty="basic"):
        """
        Initialize the ComputerIntelligence object.

        Args:
            difficulty (str, optional): The difficulty level of the computer intelligence.
            becomes "basic"
        """
        super().__init__("Computer")
        self.difficulty = difficulty

    def take_turn(self, round_score):
        """
        Make a decision on whether to roll or hold based on the current round score.

        Args:
            round_score (int): The current score in this round.

        Returns:
            str: The decision, either it is "roll" or "hold".
        """

        if self.difficulty == "basic":
            decision = self.basic_strategy(round_score)
            print(f"Computer chose: {decision}")
            return decision
        elif self.difficulty == "advanced":
            decision = self.advanced_strategy(round_score)
            print(f"Computer chose: {decision}")
            return decision
        else:
            raise ValueError("Invalid Difficulty Level")

    def basic_strategy(self, round_score):
        """
        Make a decision based on a simple threshold for the basic strategy.

        Args:
            round_score (int): The current score in the round.

        Returns:
            str: The decision either "roll" or "hold"
        """
        # Simple threshold for basic strategy
        if round_score < 25:
            return "roll"
        else:
            return "hold"

    def advanced_strategy(self, round_score):
        """
        Make a decision based on an advanced strategy which considers the current score.

        Args:
            round_score (int): The current score in the round.

        Returns:
            str: The decision either "roll" or "hold"
        """
        if round_score >= 75:  # If current score is close to winning, hold
            return "hold"
        elif round_score < 30:  # If current score is low, roll
            return "roll"
        else:
            # Random decision if neither condition is meet
            return choice(["roll", "hold"])
