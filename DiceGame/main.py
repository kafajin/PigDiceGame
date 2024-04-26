"""main module"""
import sys
from player import Player
from game import Game
from dice import Dice
from computer_intelligence import ComputerIntelligence
from highscore import HighScore


def main():
    """Function to start and control the Pig Dice Game."""
    print("------------------------------")
    print("|        Pig Dice Game        |")
    print("------------------------------")

    # Print the rules of the game
    print("\nRules of the Pig Dice Game:")
    print("Each turn, a player repeatedly rolls a die until either a"
          " is rolled or the player decides to 'hold':")
    print("- If the player rolls a 1, they score nothing "
          "and it becomes the next player's turn.")
    print("- If the player rolls any other number,"
          "it is added to their turn total and the player's turn continues.")
    print("- If a player chooses to 'hold',their turn total is added "
          "to their score, and it becomes the next player's turn.")
    print("- If a player chooses to 'quit', the game turminates.")
    print("- If a player chooses to 'cheat', the player wins directly.")
    print("\nThe first player to score 100 or more points wins.")

    # instantiate HighScore class
    high_scores = HighScore()

    try:
        while True:
            player_choice = input("\nDo you want to play against another human or computer? (human/computer): ").lower()

            if player_choice == "human":
                human_player1 = Player("")  # Initialize with an empty name
                human_player1.select_name()  # Human player 1 selects name

                # Ask if the player wants to change their name
                while True:
                    change_name_decision = input(f"Do you want to change {human_player1.name}'s name? (yes/no): ").lower()
                    if change_name_decision == "yes":
                        new_name = input(f"Please enter {human_player1.name}'s new name: ")
                        try:
                            human_player1.change_name(new_name)
                            print(f"Name changed successfully to {new_name}\n")
                            break
                        except ValueError as e:
                            print(f"Error: {e}")
                    elif change_name_decision == "no":
                        print(f"Keeping {human_player1.name}'s current name.")
                        break
                    else:
                        print("Please answer with 'yes' or 'no'.")

                print(f"\n- Human Player 1: {human_player1.name}")

                human_player2 = Player("")  # Initialize with an empty name
                human_player2.select_name()  # Human player 2 selects name

                # Ask if the player wants to change their name
                while True:
                    change_name_decision = input(f"Do you want to change {human_player2.name}'s name? (yes/no): ").lower()
                    if change_name_decision == "yes":
                        new_name = input(f"Please enter {human_player2.name}'s new name: ")
                        try:
                            human_player2.change_name(new_name)
                            print(f"Name changed successfully to {new_name}\n")
                            break
                        except ValueError as e:
                            print(f"Error: {e}")
                    elif change_name_decision == "no":
                        print(f"Keeping {human_player2.name}'s current name.")
                        break
                    else:
                        print("Please answer with 'yes' or 'no'.")

                print(f"\n- Human Player 2: {human_player2.name}")

                game_instance = Game(
                    [human_player1, human_player2],
                    Dice(), high_scores)

            elif player_choice == "computer":
                human_player = Player("")  # Initialize with an empty name
                human_player.select_name()  # Human player selects name

                # Ask if the player wants to change their name
                while True:
                    change_name_decision = input(f"Do you want to change {human_player.name}'s name? (yes/no): ").lower()
                    if change_name_decision == "yes":
                        new_name = input(f"Please enter {human_player.name}'s new name: ")
                        try:
                            human_player.change_name(new_name)
                            print(f"Name changed successfully to {new_name}\n")
                            break
                        except ValueError as e:
                            print(f"Error: {e}")
                    elif change_name_decision == "no":
                        print(f"Keeping {human_player.name}'s current name.")
                        break
                    else:
                        print("Please answer with 'yes' or 'no'.")

                print(f"\n- Human Player: {human_player.name}")

                while True:
                    choice_difficulty = input("Choose computer difficulty - basic or advanced: ").lower()
                    if choice_difficulty in ["basic", "advanced"]:
                        break
                    else:
                        print("Invalid input. Choose 'basic' or 'advanced'.")

                computer_player = ComputerIntelligence(
                    difficulty=choice_difficulty)

                game_instance = Game(
                    [human_player, computer_player],
                    Dice(), high_scores)

            else:
                print("Invalid choice. Please enter 'human' or 'computer'.")
                continue

            # Load high scores
            high_scores.load_high_scores()

            # Play until one player reaches a score of 100
            while max(player.get_score() for player in game_instance.players) < 100:
                if not game_instance.play():
                    break  # Exit the loop if the play method returns False

            # Determine the winner
            max_score = max(player.get_score() for player in game_instance.players)
            winners = [
                player.name
                for player in game_instance.players
                if player.get_score() == max_score]
            print(
                f"\nCongratulations! {' and '.join(winners)} "
                f"won with {max_score} points!")

            # Display the scores
            high_scores.display_high_scores()

            # Ask if the player wants to play again
            while True:
                play_again = input("Do you want to play again? (yes/no): ").lower()
                if play_again == "yes":
                    # Restart the game or perform any other necessary action
                    print("Restarting the game...")
                    break  # Exit the loop and proceed with the game restart
                elif play_again == "no":
                    print("Thanks for playing! Goodbye!")
                    sys.exit()  # Exit the program
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
    except KeyboardInterrupt:
        print("\nGame interrupted. Exiting...")
        sys.exit()


if __name__ == "__main__":
    main()
