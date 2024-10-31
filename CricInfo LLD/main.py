from match import Match
from TeamScore import TeamScoreCard
from team import Team
from players import Players
from constants import PlayerRole, BallResult

team_a = Team("India")
team_b = Team("Australia")
team_a_scorecard = TeamScoreCard()
team_b_scorecard = TeamScoreCard()
match = Match(team_a, team_b, team_a_scorecard,team_b_scorecard)
# Team India Players
virat = Players("Virat", PlayerRole.BATSMAN)
dhawan = Players("Dhawan", PlayerRole.BATSMAN)
rohit = Players("Dhawan", PlayerRole.BATSMAN)
raina = Players("Raina", PlayerRole.ALL_ROUNDER)
yuvraj = Players("Yuvraj", PlayerRole.ALL_ROUNDER)
zaheer = Players("Zaheer", PlayerRole.BOWLER)
kumble = Players("Kumble", PlayerRole.BOWLER)
dhoni = Players("Dhoni", PlayerRole.BATSMAN)

# Team Australia players
ponting = Players("Ponting", PlayerRole.BATSMAN)
waugh = Players("Steve Waugh", PlayerRole.BATSMAN)
watson = Players("Watson", PlayerRole.ALL_ROUNDER)
lee = Players("Lee", PlayerRole.BOWLER)
hayden = Players("Hayden", PlayerRole.BATSMAN)
gilchrist = Players("Gilchrist", PlayerRole.BATSMAN)
warne = Players("Warne", PlayerRole.BOWLER)


india_players = [Players("Virat", PlayerRole.BATSMAN), Players]
match.start_match(
    1,1,[virat, raina, rohit, dhoni, zaheer, kumble], [gilchrist, hayden, ponting, lee,warne],
[dhawan, yuvraj], [watson, waugh]
)
match.initialize_innings(1, virat, raina, lee)
match.show_score()
match.ball_bowled(BallResult.SINGLE)
match.ball_bowled(BallResult.SINGLE)
match.show_score()
