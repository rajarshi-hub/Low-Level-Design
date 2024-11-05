



class Tournaments:

    def __init__(self):
        self.matches = []
        self.participating_teams = {}  # dictionary for team and their state for matches won, lost and No result

    def get_match(self, index):
        try:
            return self.matches[index]
        except IndexError:
            raise "Match is not available"
