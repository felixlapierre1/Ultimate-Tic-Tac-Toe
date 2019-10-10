import argparse
import copy
from contextlib import contextmanager
import importlib
import signal

from game import Game


def raise_timeout(signum, frame):
    raise TimeoutError


if __name__ == "__main__":

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
    bots.append(bot1())

    mod = importlib.import_module(args.bot2)
    bot2 = getattr(mod, "bot")
    bots.append(bot2())

    # Start game
    TIME_OUT_TIME = 1
    if args.verbose:
        TIME_OUT_TIME = 300

    timed_out = False
    forced_move = list(game.map_tile)
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
            player_move = bots[game.player_turn].move(
                copy.deepcopy(game.board), copy.copy(forced_move)
            )
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
