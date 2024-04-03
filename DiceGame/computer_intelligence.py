from random import choice
from player import Player


class ComputerIntelligence(Player):
    def __init__(self, difficulty="basic"):
        super().__init__("Computer")
        self.difficulty = difficulty

    def take_turn(self, current_score, round_score):
        if self.difficulty == "basic":
            decision = self.basic_strategy(round_score)  # current_score
            print(f"Computer chose: {decision}")
            return decision
        elif self.difficulty == "advanced":
            decision = self.advanced_strategy(current_score, round_score)
            print(f"Computer chose: {decision}")
            return decision
        else:
            raise ValueError("Invalid Difficulty Level")

    def basic_strategy(self, round_score):
        # Simple threshold for basic strategy
        if round_score < 20:
            return "roll"
        else:
            return "hold"

    def advanced_strategy(self, current_score):
        # Advanced strategy: can be more nuanced based on current score
        if current_score >= 70:  # If current score is close to winning, hold
            return "hold"
        elif current_score < 30:  # If current score is low, roll
            return "roll"
        else:
            # Random decision if neither condition is meet
            return choice(["roll", "hold"])