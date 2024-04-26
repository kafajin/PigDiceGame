import random

# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
# ● ┌ ─ ┐ │ └ ┘
# The art was taken from a youtube video │ DICE ROLLER program in python
# https://www.youtube.com/watch?v=x-Ag2_bJ40Y&ab_channel=BroCode │

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}


class Dice:
    """""Class Reprensting a dice."""
    @staticmethod
    def roll_dice():
        """
        Sumilates rolling a dice and prints it's face.

        Returns:
            int: The value of the rolled dice (1-6).
        """
        die = random.randint(1, 6)
        for line in Dice.show_dice(die):
            print(line)  # Print each line of the dice art
        return die

    @staticmethod
    def show_dice(value):
        """
        Gets the Unicode art representation of a specific dice face.

        Returns:
            tuple of str: Tuple containing lines of the Unicode art representing the dice face.

        """
        return dice_art[value]
