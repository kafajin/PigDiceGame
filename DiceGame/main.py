from player import Player
from game import Game
from dice import Dice
from computer_intelligence import ComputerIntelligence


def main():
    print("------------------------------")
    print("|        Pig Dice Game        |")
    print("------------------------------")

    # Print the rules of the game
    print("\nRules of the Pig Dice Game:")
    print("Each turn, a player repeatedly rolls a die until either a 1 is rolled or the player decides to 'hold':")
    print("- If the player rolls a 1, they score nothing and it becomes the next player's turn.")
    print("- If the player rolls any other number, it is added to their turn total and the player's turn continues.")
    print("- If a player chooses to 'hold', their turn total is added to their score, and it becomes the next player's turn.")
    print("\nThe first player to score 50 or more points wins.")

    while True:
        human_player = Player("")  # Initialize with an empty name
        human_player.select_name()  # Human player selects name
        print(f"\n- Human Player: {human_player.name}")

        # Adding an option for the player to change their name
        while True:
            change_name_decision = input("Do you want to change your name? (yes/no): ").lower()
            if change_name_decision == "yes":
                new_name = input("Please enter your new name: ")
                try:
                    human_player.change_name(new_name)
                    print(f"Name changed successfully to {new_name}\n")
                except ValueError as e:
                    print(f"Error: {e}")
                break
            elif change_name_decision == "no":
                print("Keeping the current name.")
                break
            else:
                print("Please answer with 'yes' or 'no'.")

                     # Ask for computer difficulty
        while True:  # This loop ensures that the user inputs either 'basic' or 'advanced'
            choice_difficulty = input("\nChoose computer difficulty - basic or advanced: ").lower()
            if choice_difficulty in ["basic", "advanced"]:
                break
            else:
                print("Invalid input. Please choose 'basic' or 'advanced'.")

        # Initialize computer player with chosen difficulty
        computer_player = ComputerIntelligence(difficulty=choice_difficulty)

        game_instance = Game([human_player, computer_player], Dice())  # Pass players list and Dice instance separately

        # Play until one player reaches a score of 50
        while max(player.score for player in [human_player, computer_player]) < 50:
            game_instance.play()

        # Determine the winner
        max_score = max(player.score for player in [human_player, computer_player])
        winners = [player.name for player in [human_player, computer_player] if player.score == max_score]
        print(f"\nCongratulations! {' and '.join(winners)} won with {max_score} points!")

        # Ask if the player want to play again
        play_again = input("DO you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break  # exit the loop if the player doesnt want to play again


if __name__ == "__main__":
    main()