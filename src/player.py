from src.dice import roll_dice


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

    def move(self, squares: int = None) -> int:
        """Moves the player by the given number of squares.
        If no number is given, the player will roll a dice and move acording to the results.
        """

        # input("Press any key to roll the dice...")

        if not squares:
            squares = self.roll_dice()

        self.position += squares
        return squares

    def roll_dice(self):
        """Rolls a dice and returns the result.
        This method is here because we may want to change the way the player rolls the dice.
        """
        return roll_dice()
