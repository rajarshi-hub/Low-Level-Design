
from constants import InningsOrder, InningsState, BallResult
from stats import BowlingStat, BattingStat


class TeamScoreCard:

    def __init__(self):
        self.runs = 0
        self.wickets = 0
        self.extras = 0
        self.overs = 0
        self.balls = 0
        self.innings_state = InningsState.UPCOMING
        self.innings_order = InningsOrder.UNDECIDED
        self.bowling_scorecard = {}   # Dict players: BowlStat
        self.batting_scorecard = {}   # Dict players: BatStat

    def initialize_players(self, players):
        for player in players:
            self.batting_scorecard[player] = BattingStat()
            self.bowling_scorecard[player] = BowlingStat()

    def update_team_batting(self, batsman, result):
        for cur_batsman in self.batting_scorecard:
            if cur_batsman == batsman:
                # TODO: Update 4s and 6s for the batsman accordingly
                self.batting_scorecard[cur_batsman].runs += result
                return

    def update_bating_score(self, result, batsman):
        # TODO: Handling all cases for all the cases of ball bowled
        if result == BallResult.DOT:
            self.balls += 1
        if result == BallResult.SINGLE:
            self.balls += 1
            self.runs += BallResult.SINGLE.value
        elif result == BallResult.SIX:
            self.balls += 1
            self.runs += BallResult.SIX.value
        self.update_team_batting(batsman, result.value)
        if self.balls == 6:
            self.balls = 0
            self.overs += 1

    def is_over_ended(self):
        return self.balls == 0

    def show_score(self):
        print('---------------------------------')
        print("{runs}/{wicket}".format(runs=self.runs, wicket=self.wickets))
        print('---------------------------------')
        print("{overs}.{balls}".format(overs=self.overs, balls=self.balls))
        print('#################################')
        for batsman in self.batting_scorecard:
            print(batsman.name, '--- Runs --->',  self.batting_scorecard[batsman].runs, '\n')
