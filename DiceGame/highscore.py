class HighScore:
    def __init__(self, filename="high_score.txt"):
        self.filename = filename
        self.high_scores = {}

    def load_high_scores(self):
        # load high scores from the file
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    player, score = line.strip().split(":")
                    self.high_scores[player] = int(score)
        except FileNotFoundError:
            # if the file doesnt exist, create an emoty high_scores dictionary
            self.high_scores = {}
    
    def save_high_scores(self):
        # save the high scores to the file
        with open(self.filename, "w") as file:
            for player, score in self.high_scores.items():
                file.write(f"{player}:{score}\n")
    
    def update_high_scores(self, winner_name, winner_score):
        # Update high scores with the latest game result
        if winner_name in self.high_scores:
            if winner_score > self.high_scores[winner_name]:
                self.high_scores[winner_name] = winner_score
    
    def display_high_scores(self):
        print("High Scores:")
        if self.high_scores:
            for player, score in self.high_scores.items():
                print(f"{player}: {score}")
        else:
            print("No high scores to display.")