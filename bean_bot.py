"""
This is the ONLY file you should modify.

(1) Name this file with your teamname:
    Do not include space in the filename.

(2) Send this file at the end of the tryout for submission.

"""
import random

moves = ["NW", "N", "NE", "W", "C", "E", "SW", "S", "SE"]


class bot:
    my_letter = "?"
    last_move = ("?", "?")

    def __init__(self):
        self.team_name = "BeanBotV1"

    def move(self, game, forced_move):
        "Logic for your bot"
        # Hack to figure out if im X or O
        if self.last_move[0] != "?":
            self.my_letter = game[self.map_tile[self.last_move[0]]
                                  ][self.map_tile[self.last_move[1]]]

        # Pick one of the possible big squares at random
        if len(forced_move) == 0:
            return ("C", "C")
        bigMove = forced_move[random.randint(0, len(forced_move) - 1)]

        # Pick a move in the little square that wins, if we can
        for move in moves:
            tile = game[self.map_tile[bigMove]]
            if self.is_winning_move(game, tile, move):
                return (bigMove, move)

        # Pick one of the possible little squares at random
        lilMove = random.randint(0, 8)

        self.last_move = (bigMove, moves[lilMove])
        return (self.last_move)

    def is_winning_move(self, game, tile, move):
        if "." != tile[self.map_tile[move]]:
            return False
        _tile = tile.copy()
        _tile[self.map_tile[move]] = self.my_letter
        return self.check_win(_tile)

    def check_win(self, tile):
        tick = self.my_letter

        # Horizontal
        for i in range(3):
            if all(tick == x for x in tile[i * 3: (i * 3) + 3]):
                return True

        # Vertical
        for i in range(3):
            if all(tick == x for x in tile[[i, i + 3, i + 6]]):
                return True

        # Diagonal
        return all(tick == x for x in tile[[0, 4, 8]]) or all(
            tick == x for x in tile[[2, 4, 6]]
        )

    map_tile = {
        "NW": 0,
        "N": 1,
        "NE": 2,
        "W": 3,
        "C": 4,
        "E": 5,
        "SW": 6,
        "S": 7,
        "SE": 8,
    }
