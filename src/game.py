from src.player import Player
from src.board_config import config


MIN_PLAYERS = 1
MAX_PLAYERS = 10


class Game:
    """Represents a game of Ladders and Snakes."""

    def __init__(
        self,
        players_count: int,
        board_config: dict = config,
        wait_for_user: bool = True,
    ):
        """Initializes a new game with the given number of players.
        Raises:
            ValueError: If the number of players is not within the allowed range.
            ValueError: If the board config is invalid.
        """

        try:
            if not MIN_PLAYERS <= players_count <= MAX_PLAYERS:
                raise ValueError(
                    f"""Minimum of players for this game is {MIN_PLAYERS} and maximum is {MAX_PLAYERS}. You entered {players_count}.
                    If you want to change the limits, you can change the constants MIN_PLAYERS and MAX_PLAYERS in the game.py."""
                )

            self.wait_for_user: bool = wait_for_user
            self.players: list[Player] = self.create_players(players_count)

            self.user_start = 0
            self.board: list[int] = self.create_board(board_config)

            print("Wait for user: ", wait_for_user)
            self.current_player_index: int = 0
            self.round: int = 0
            self.winner: Player = None
            self.created_properly: bool = True

        except Exception as exception:
            print("Game was not created properly.")
            print(exception)
            print("Please try again with valid parameters.")
            raise

    @property
    def current_player(self) -> Player:
        """Returns the current player."""
        return self.players[self.current_player_index]

    def user_view_position(self, player: Player) -> int:
        """Returns the position of the given player from the user's point of view.
        We need to view the position for the user because the board is zero-indexed in the program, but usually one-indexed for the user.
        """
        return player.position + self.user_start

    # CREATION METHODS

    def create_players(self, count: int) -> list[Player]:
        """Creates the players of the game."""

        # Here we can have other options for the players, like their nicknames, colors, etc.
        return [Player(i + 1, self.wait_for_user) for i in range(count)]

    def create_board(self, board_config: dict) -> list[int]:
        """Loads the board from the given config file.
        The board is a list of integers, where each index represents a square.
        The value of each index represents the index of the square where the player will be moved.
        Some squares are special, so the player will be moved to another square.
        Some are not special, so the player will be moved to the same square or not moved at all.
        """

        try:
            # check if the board config is valid before creating the board
            if (
                "start" not in board_config
                or "end" not in board_config
                or "special_squares" not in board_config
            ):
                raise ValueError("Invalid board config: Missing required keys.")

            # processing the board config
            start: int = board_config["start"]
            self.user_start = start
            end: int = board_config["end"]
            size = end - start + 1

            # fill the board with the default values
            board: list[int] = [i for i in range(size)]

            # set the special squares
            for user_index_from, user_index_to in board_config[
                "special_squares"
            ].items():
                board_index_from = int(user_index_from) - start
                board_index_to = user_index_to - start
                board[board_index_from] = board_index_to

            # check if the board is valid after creating it
            if board[0] != 0:
                raise ValueError(
                    "Invalid board: The first square must start at index 0."
                )

            if board[-1] != end - start:
                raise ValueError()

            for square in board:
                if not 0 <= square < size:
                    raise ValueError()

        except Exception as exception:
            raise exception

        return board

    # GAMEPLAY METHODS

    def play(self):
        """Starts and plays the game."""

        try:
            while not self.winner:
                self.play_turn()
                self.set_next_player()

            print(f"Player {self.winner.number} won!")
            return self.winner

        except Exception:
            print("Something went wrong while playing the game.")
            raise

    def play_turn(self):
        """Plays a round of the game."""

        self.round += 1
        player = self.current_player

        print(f"\nRound {self.round}")
        print(f"Player {player} turn.")

        # player rolls the dice and moves
        square_count = player.move()
        position = player.position

        print(
            f"{player} rolled the dice and moved by {square_count} squares to the square {self.user_view_position(player)}."
        )

        # check if the player won
        if position == len(self.board) - 1:
            self.winner = player
            print(f"{player} won!")
            return self.winner

        # check if the player ended up out of the board
        if position >= len(self.board):
            print(f"{player} ended up out of the board.")
            print(f"{player} will be moved back by {square_count} squares.")
            player.position -= square_count
            return

        # check if the player ended up on a special square and move him accordingly
        self.correct_positions(player)

    def correct_positions(self, player: Player):
        """Corrects the position of the given player if he ended up on a special square."""

        position = player.position
        new_position = self.board[position]

        if new_position != position:
            player.move_to(new_position)
            print(
                f"{player} ended up on a special square and was moved to square {self.user_view_position(player)}."
            )

        # if the player ended up on the same square as another player,
        # the other player the other player will be moved backwards by one square
        for other_player in self.players:
            if other_player == player:
                continue

            if other_player.position == player.position:
                other_player.position -= 1
                print(
                    f"{other_player} was moved back by one square and is now at square {self.user_view_position(other_player)}."
                )

                # check if the other player ended up on a special square again
                self.correct_positions(other_player)

    def set_next_player(self):
        """Sets current player the next player."""

        next_player_index = (self.current_player_index + 1) % len(self.players)
        self.current_player_index = next_player_index
        return self.current_player
