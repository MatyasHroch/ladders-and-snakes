from src.game import Game


if __name__ == "__main__":
    # Test script 1
    game = Game(5, wait_for_user=True)
    winner = game.play()
    print(winner)

    # # Test script 2
    # winners = [Game(4, wait_for_user=False).play() for _ in range(100)]
    # [print(winner) for winner in winners]
    # input("Press Enter to exit...")
