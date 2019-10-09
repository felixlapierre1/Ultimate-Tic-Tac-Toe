import argparse
from contextlib import contextmanager
import importlib
import signal

from game import Game


<<<<<<< HEAD
@contextmanager
def timeout(time):
    # Register a function to raise a TimeoutError on the signal.
    # signal.signal(signal.SIGALRM, raise_timeout)
    # Schedule the signal to be sent after ``time``.
    # signal.alarm(time)

    try:
        yield
    except TimeoutError:
        pass
    finally:
        # Unregister the signal so it won't be triggered
        # if the timeout is not reached.
        pass
        # signal.signal(signal.SIGALRM, signal.SIG_IGN)


=======
>>>>>>> 0274c688530f17136baabb436193c7de3b7098f9
def raise_timeout(signum, frame):
    raise TimeoutError


if __name__ == "__main__":
    import sys
    import my_bot
    print(sys.path)
    parser = argparse.ArgumentParser(description="CS GAMES 2020 AI Tryout")
    parser.add_argument("bot1", type=str, help="filename")
    parser.add_argument("bot2", type=str, help="filename")
    parser.add_argument("--verbose", action="store_true", help="display the gameboard")
    args = parser.parse_args()

    # Import bot class
    game = Game()
    bots = list()
    mod = importlib.import_module(args.bot1)
    bot1 = getattr(mod, "bot")
    bots.append(bot1(game))

    mod = importlib.import_module(args.bot2)
    bot2 = getattr(mod, "bot")
    bots.append(bot2(game))

    # Start game
    TIME_OUT_TIME = 1
    if args.verbose:
        TIME_OUT_TIME = 300

    timed_out = False
    forced_move = game.map_tile.keys()
    while True:

        # Next player's turn
        game.player_turn = (game.player_turn + 1) % 2
        if args.verbose:
            game.status()

        if timed_out:
            print(f"\n{bots[game.player_turn].team_name} won!!!")
            break  # Opponent timed out

        timed_out = True
        # Validate player's move
        while True:
            player_move = bots[game.player_turn].move()
            if player_move[0] not in forced_move:
                continue

            try:
                if game.make_move(*player_move):
                    forced_move = game.next_tile
                    break
            except Exception:
                print("Invalid move")
        timed_out = False

        # Check for win
        if game.check_win(game.board[Game.map_tile[player_move[0]]]):
            tick = "X" if game.player_turn == 0 else "O"
            game.win_status[Game.map_tile[player_move[0]]] = tick

            if player_move[0] == player_move[1]:
                game.next_tile = [
                    tile
                    for i, tile in enumerate(Game.map_tile.keys())
                    if game.win_status[i] is None
                ]
                forced_move = game.next_tile

            if game.check_win(game.win_status):
                print(
                    f"\n{bots[game.player_turn].team_name} won!!!"
                )  # Winning sequence
                break
