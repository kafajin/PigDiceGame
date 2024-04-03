class Player:
    # Simple class with 'name', 'score' and round_score as attributes.
    def __init__(self, name):
        self.name = name
        self.score = 0
        # self.round_score = 0

    def reset_score(self):
        self.score = 0

    def add_score(self, points):
        self.score += points

    def get_score(self):
        return self.score
    
    # below for human player
    def take_turn(self, dice):
        print(f"It's {self.name}'s turn.")
        roll = input("Roll or Hold? (r/h): ").lower()
        if roll == 'r':
            dice_roll = dice.roll_dice()
            print(f"{self.name} rolled a {dice_roll}.")
            if dice_roll == 1:
                print("You rolled a 1. No points gained this turn.")
                self.reset_score()
                return False
              
            else:
                self.add_score(dice_roll)
                print(f"Your current score: {self.get_score()}")
        elif roll == 'h':
            print(f"{self.name} chose to hold.")
            return False
        else:
            print("Invalid input. Please enter 'r' to roll or 'h' to hold.")

    # Method for selecting a name
    def select_name(self):
        human_name = input("\nPlease enter your name: ")
        if not human_name:
            print("Name cannot be empty ")
        else:
            self.name = human_name
            print(f"Player's name set to {human_name}.")

    # Method for changing name.
    def change_name(self, new_playername):
        if not new_playername:
            raise ValueError("Name cannot be empty. Please enter a name.")
        else:
            old_name = self.name
            self.name = new_playername
            print(f"Player's name changed from {old_name} to {new_playername}")

    # Method for holding the score.
    def hold(self):
        self.score += self.round_score
        self.round_score = 0