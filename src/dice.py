import random

DICE_MAX = 6


def roll_dice(dice_max=DICE_MAX, repeat=True):
    """Rolls an imaginary dice and returns the result."""

    result = random.randint(1, dice_max)

    print(f"Dice result: {result}")

    # repeats the roll if the result is the maximum value
    if repeat and result == dice_max:
        print(f"Rolling again!")
        return result + roll_dice()

    return result
