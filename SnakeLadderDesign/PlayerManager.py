class PlayerManager:
    players_list = []
    turn = 0

    def __init__(self, players):
        self.players_list = players

    def get_player(self):
        cur_player = self.players_list[self.turn]
        self.turn += 1
        self.turn = self.turn % len(self.players_list)
        return cur_player
