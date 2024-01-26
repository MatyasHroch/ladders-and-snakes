from .dice import roll_dice


class Player:
    """Represents a player of Snakes and Ladders."""

    def __init__(self, number: int):
        """Initializes a new player with the given number as his identificator."""

        self.number = number
        self.position = 0

    def __str__(self):
        """Returns the string representation of the player."""

        return f"Player {self.number}"

    def move_to(self, new_position: int):
        """Moves the player to the given position."""

        if new_position < 0:
            raise ValueError("The new position must be a positive integer.")

        self.position = new_position

    def move(self, squares: int = None):
        """Moves the player by the given number of squares.
        If no number is given, the player will roll a dice and move acording to the results.
        """

        input("Press any key to roll the dice...")

        if not squares:
            squares = self.roll_dice()

        self.position += squares

        print(f"{self} moved {squares} squares and is now at square {self.position}.")

        return squares

    def roll_dice(self):
        """Rolls a dice and returns the result."""

        return roll_dice()
