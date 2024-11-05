

class Team:

    def __init__(self, team_name):
        self.playing_eleven = []   # Player Class
        self.reserves = []         # Player Class
        self.team_name = team_name

    def assign_players(self, players, reserves):
        self.playing_eleven = players
        self.reserves = reserves
