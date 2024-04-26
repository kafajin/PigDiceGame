import unittest
from computer_intelligence import ComputerIntelligence

class TestComputerIntelligence(unittest.TestCase):
    def test_basic_strategy_below_threshold(self):
        computer = ComputerIntelligence(difficulty="basic")
        decision = computer.basic_strategy(round_score=20)
        self.assertEqual(decision, "roll")

    def test_basic_strategy_above_threshold(self):
        computer = ComputerIntelligence(difficulty="basic")
        decision = computer.basic_strategy(round_score=30)
        self.assertEqual(decision, "hold")

    def test_advanced_strategy_close_to_winning(self):
        computer = ComputerIntelligence(difficulty="advanced")
        decision = computer.advanced_strategy(round_score=80)
        self.assertEqual(decision, "hold")

    def test_advanced_strategy_low_score(self):
        computer = ComputerIntelligence(difficulty="advanced")
        decision = computer.advanced_strategy(round_score=20)
        self.assertEqual(decision, "roll")

    def test_advanced_strategy_random_decision(self):
        computer = ComputerIntelligence(difficulty="advanced")
        # Since neither condition is met, decision should be random between "roll" and "hold"
        decision = computer.advanced_strategy(round_score=50)
        self.assertIn(decision, ["roll", "hold"])

if __name__ == '__main__':
    unittest.main()
