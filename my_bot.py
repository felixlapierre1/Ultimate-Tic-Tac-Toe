"""
This is the ONLY file you should modify.

(1) Name this file with your teamname:
    Do not include space in the filename.

(2) Send this file at the end of the tryout for submission.

"""


class bot:
    def __init__(self):
        self.team_name = "Foo"

    def move(self, game, forced_move):
        "Logic for your bot"

        return input("Enter a move (e.g. NW/SE): ").strip().split("/")
