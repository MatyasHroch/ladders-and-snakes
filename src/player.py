from src.dice import roll_dice


class Player:
    """Represents a player of Snakes and Ladders."""

    def __init__(self, number: int, wait_for_user: bool = True):
        """Initializes a new player with the given number as his identificator.
        If we want just simulate a user playing the game, we can set wait_for_user to False.
        """

        self.number = number
        self.wait_for_user = wait_for_user
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

        if self.wait_for_user:
            input("Press ENTER to roll the dice...")

        if not squares:
            squares = self.roll_the_dice()

        self.position += squares
        return squares

    def roll_the_dice(self):
        """Rolls a dice and returns the result.
        This method is here because we may want to change the way the player rolls the dice.
        """
        return roll_dice()
