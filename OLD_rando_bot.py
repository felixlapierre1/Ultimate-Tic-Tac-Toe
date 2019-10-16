"""
This is the ONLY file you should modify.

(1) Name this file with your teamname:
    Do not include space in the filename.

(2) Send this file at the end of the tryout for submission.

"""
import random

moves = ["NW", "N", "NE", "W", "C", "E", "SW", "S", "SE"]

class bot:
    def __init__(self):
        self.team_name = "RandoBot"

    def move(self, game, forced_move):
        "Logic for your bot"

        bigMove = random.randint(0, 8)
        lilMove = random.randint(0, 8)

        return (moves[bigMove], moves[lilMove])
