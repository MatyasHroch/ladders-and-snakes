from .player import Player
from .board_config import config


MIN_PLAYERS = 1
MAX_PLAYERS = 10


class Game:
    """Represents a game of Ladders and Snakes."""

    def __init__(self, players_count: int, board_config: dict = config):
        """Initializes a new game with the given number of players."""

        if not MIN_PLAYERS <= players_count <= MAX_PLAYERS:
            raise ValueError(
                f"Minimum of players for this game is {MIN_PLAYERS} and maximum is {MAX_PLAYERS}."
            )

        self.players: list[Player] = self.create_players(players_count)

        self.start = 0
        self.board: list[int] = self.create_board(board_config)

        self.current_player_index: int = 0
        self.round: int = 0
        self.winner: Player = None

    @property
    def current_player(self) -> Player:
        """Returns the current player."""
        return self.players[self.current_player_index]

    # CREATION METHODS

    def create_players(self, count: int) -> list[Player]:
        """Creates the players of the game."""
        # Here we can have other options for the players, like their names, colors, etc.
        return [Player(i + 1) for i in range(count)]

    def create_board(self, board_config: dict) -> list[int]:
        """Loads the board from the given config file.
        The board is a list of integers, where each index represents a square.
        The value of each index represents the index of the square where the player will be moved.
        Some squares are special, so the player will be moved to another square.
        Some are not special, so the player will be moved to the same square or not moved at all.
        """

        try:
            start = board_config["start"]
            self.start = start
            end = board_config["end"]
            size = end - start + 1

            # fill the board with 0s
            board: list[int] = [i for i in range(size)]

            for user_index_from, user_index_to in board_config[
                "special_squares"
            ].items():
                board_index_from = int(user_index_from) - start
                board_index_to = user_index_to - start

                board[board_index_from] = board_index_to

        except Exception as exception:
            raise ValueError("Invalid board config file.") from exception

        return board

    # GAMEPLAY METHODS

    def play(self):
        """Starts and plays the game."""
        try:
            while not self.winner:
                self.play_turn()
                self.next_player()

            print(f"Player {self.winner.number} won!")

        except Exception as exception:
            print(exception)

    def play_turn(self):
        """Plays a round of the game."""
        self.round += 1
        player = self.current_player

        print(f"Round {self.round}")
        print(f"Player {player} turn.")

        # player rolls the dice and moves
        square_count = player.move()
        position = player.position

        # check if the player won
        if position == len(self.board) - 1:
            self.winner = player
            return

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

        # if the player ended up on the same square as another player,
        # the other player the other player will be moved backwards by one square
        for other_player in self.players:
            if other_player == player:
                continue

            if other_player.position == player.position:
                other_player.position -= 1
                print(
                    f"{other_player} was moved back by one square and is now at square {other_player.position}."
                )

                # check if the other player ended up on a special square again
                self.correct_positions(other_player)

    def next_player(self):
        """Moves to the next player."""
        next_player_index = (self.current_player_index + 1) % len(self.players)
        self.current_player_index = next_player_index
