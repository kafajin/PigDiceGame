import sys


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def reset_score(self):
        self.score = 0

    def add_score(self, points):
        self.score += points

    def get_score(self):
        return self.score

    def take_turn(self, dice):
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
        human_name = input("\nPlease enter your name: ")
        if not human_name:
            print("Name cannot be empty ")
        else:
            self.name = human_name
            print(f"Player's name set to {human_name}.")

    def change_name(self, new_playername):
        if not new_playername:
            raise ValueError("Name cannot be empty. Please enter a name.")
        else:
            old_name = self.name
            self.name = new_playername
            print(f"Player's name changed from {old_name} to {new_playername}")

    def hold(self):
        self.round_score = 0
        self.score += self.round_score
