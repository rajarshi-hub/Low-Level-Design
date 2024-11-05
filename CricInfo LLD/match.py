
from constants import MatchState, InningsOrder, BallResult


class Match:

    def __init__(self, team_a, team_b, team_a_scorecard, team_b_scorecard):
        self.team_a = team_a    # Team Class
        self.team_b = team_b    # Team Class
        self.match_state = MatchState.UPCOMING       # Match state Enum     # we can use state design pattern
        self.toss = 0  # 1 -- TeamA   2 -- TeamB
        self.innings = 0  # first or second innings
        self.batting_team = None
        self.bowling_team = None
        self.batting_first = 0
        self.team_a_scorecard = team_a_scorecard    # TeamScoreBoard Class
        self.team_b_scorecard = team_b_scorecard    # TeamScoreBoard Class
        self.live_commentary = []                   # Commentary Class
        self.strike_batsman = None
        self.non_strike_batsman = None
        self.bowler = None

    def assign_batting_bowling_team(self):
        if self.batting_first == InningsOrder.FIRST:
            if self.innings == InningsOrder.FIRST:
                self.bowling_team = self.team_b_scorecard
                self.batting_team = self.team_a_scorecard
            else:
                self.batting_team = self.team_b_scorecard
                self.bowling_team = self.team_a_scorecard
        else:
            if self.innings == InningsOrder.FIRST:
                self.bowling_team = self.team_a_scorecard
                self.batting_team = self.team_b_scorecard
            else:
                self.batting_team = self.team_a_scorecard
                self.bowling_team = self.team_b_scorecard

    def start_match(self, toss, batting_first, team_a_players, team_b_players, team_a_reserves, team_b_reserves):
        self.toss = toss
        self.batting_first = batting_first
        self.team_a.assign_players(team_a_players, team_a_reserves)
        self.team_a.assign_players(team_b_players, team_b_reserves)

    def initialize_innings(self, innings, striker, non_striker, bowler):
        self.innings = innings
        self.assign_batting_bowling_team()
        self.strike_batsman = striker
        self.non_strike_batsman = non_striker
        self.bowler = bowler

    def initialize_over(self, bowler):
        self.bowler = bowler
        self.strike_batsman, self.non_strike_batsman = self.non_strike_batsman, self.strike_batsman

    def ball_bowled(self, result, batsman=None, bowler=None):
        # TODO: Process result of ball and update [Handling all cases] --
        # Striker, non striker, bowler [if over changed], batting team scorecard, overs, extras etc.
        self.batting_team.update_bating_score(result, self.strike_batsman)
        # TODO: Updating Bowling stat of the bowler
        if result == BallResult.DOT:
            pass
        if result == BallResult.SINGLE:
            self.strike_batsman, self.non_strike_batsman = self.non_strike_batsman, self.strike_batsman
        elif result == BallResult.SIX:
            pass
        elif result == BallResult.WICKET:
            self.strike_batsman = batsman

        if self.batting_team.is_over_ended():
            self.initialize_over(bowler)

    def show_score(self):
        self.batting_team.show_score()
