# Pig Dice Game

Welcome to the Pig Dice Game! This game is a simple and entertaining dice game where players compete to be the first to reach a target score. It's a great way to have fun and test your luck!

## Game Overview

In the Pig Dice Game, players take turns rolling a dice. Each player's turn consists of repeatedly rolling the dice until either a 1 is rolled or the player decides to "hold", "quit" or "cheat". Here are the basic rules:

- If a player rolls a 1, they score nothing for that turn, and it becomes the next player's turn.
- If a player rolls any other number (2-6), that number is added to their turn total, and the player's turn continues.
- If a player chooses to "hold," their turn total is added to their overall score, and it becomes the next player's turn.
- If a player chooses to "quit", the game turminates.
- If a player chooses to "cheat", the player wins directly.
- The first player to reach a target score (e.g., 100 points) or higher wins the game.

## Owners

This version of the Pig Dice Game is owned and maintained by:

- Shahera MR Ewaida
- Fatima Kadhem
- Nora Kafaji

## How to Play

To play the game:

1. Clone this repository to your local machine.
2. Navigate to the directory containing the game files.
3. Run the `main.py` file using Python: `python main.py`.
4. Follow the on-screen instructions to set up the game, including selecting player names and computer difficulty.
5. Roll the dice and make decisions to accumulate points and outscore your opponents.
6. The game will continue until one player reaches the target score.
7. After the game ends, you'll have the option to play again or exit.

## Features

- Interactive gameplay with both human and computer players.
- Ability to change player names and computer difficulty.
- High score tracking to keep track of the best performances.
- Option to restart the game or exit after each round.

## Computer Intelligence

The computer player in the Pig Dice Game is implemented using the `ComputerIntelligence` class. This class represents a computer player with different levels of intelligence, allowing for varying degrees of challenge in the game.

### Implementation Details

The `ComputerIntelligence` class extends the `Player` class and introduces the concept of difficulty levels. Currently, two difficulty levels are supported: "basic" and "advanced".

- In the basic strategy, the computer player follows a simple threshold approach. If the current score in the round is below a certain threshold (25 by default), the computer player continues to roll the dice. Otherwise, it chooses to hold.
- The advanced strategy considers the current score of the computer player. If the current score is close to winning (e.g., 75 or higher), the computer player chooses to hold. If the current score is low (e.g., below 30), it continues to roll. Otherwise, it makes a random decision between rolling and holding.

The decision-making process of the computer player is encapsulated in the `take_turn` method. Based on the selected difficulty level, either the basic or advanced strategy is invoked to determine whether the computer player should roll or hold.

### Usage

When starting a new game, players have the option to choose the difficulty level of the computer player. Depending on the chosen difficulty, the computer player will employ either the basic or advanced strategy during its turns.

By providing different levels of intelligence, the computer player adds an element of challenge and variability to the Pig Dice Game, making each gameplay experience unique and engaging.


## Dependencies

This game requires Python 3 to run. There are no additional dependencies.

## Contributing

We welcome contributions to improve the Pig Dice Game! If you have any ideas for new features, bug fixes, or enhancements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

Enjoy the game, and may the dice roll ever in your favor!
