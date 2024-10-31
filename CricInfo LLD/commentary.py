from constants import InningsOrder

class Commentary:

    def __init__(self, innings_order, over, ball, bowler, batsman, result):
        self.innings = innings_order
        self.over = over
        self.ball = ball
        self.bowler = bowler
        self.batsman = batsman
        self.result = result        # BallResult Enum
