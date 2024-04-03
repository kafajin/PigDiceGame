from computer_intelligence import ComputerIntelligence
from highscore import HighScore


class Game:
    def __init__(self, players, dice):
        self.players = players
        self.current_player_index = 0
        self.dice = dice
        self.high_scores = HighScore()
        self.turn = 0

    def add_player(self, player):
        self.players.append(player)

    def switch_player(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def play(self):
        print("\nWelcome to Pig Dice Game!\n")
        for player in self.players:
            print(f"Player {player.name} joined the game.")

        while all(player.get_score() < 50 for player in self.players):
            print("\n------------------------------")

            current_player = self.players[self.current_player_index]

            if isinstance(current_player, ComputerIntelligence):
                print("Computer is playing...")
                decision = current_player.take_turn(self.players[self.current_player_index - 1].get_score(), sum(player.get_score() for player in self.players))
                if decision == "roll":
                    dice_roll = self.dice.roll_dice()
                    print(f"Computer rolled a {dice_roll}.")
                    current_player.add_score(dice_roll)
                    print(f"Computer's current score: {current_player.get_score()}")
                    if dice_roll == 1:
                        print("Computer rolled a 1. No points gained this turn.")
                        current_player.reset_score()
                    else:
                        print("Computer chose to hold.")
            else:
                choice = input("Do you want to roll or hold? (r/h) or type 'q' to quit and restart the game: ").lower()
                if choice == 'q':
                    print("Quitting the current game...")
                    return True  # signal to restart the game
                elif choice == 'r':
                    current_player.take_turn(self.dice)
                elif choice == 'h':
                    print(f"{current_player.name} chose to hold.")
                    self.switch_player()

            self.switch_player()
            self.turn += 1

        winner = max(self.players, key=lambda player: player.get_score())
        print(f"\nCongratulations, {winner.name} wins with {winner.get_score()} points!")

        # Update high scores
        self.high_scores.update_high_scores(winner.name, winner.get_score())

        # Display the scores
<<<<<<< HEAD
        self.high_scores.display_high_scores()

        #testar att commita
=======
        self.high_scores.display_high_scores()
>>>>>>> 55c0f29b696d17664f2c9fa63084cf4f05b5b815
