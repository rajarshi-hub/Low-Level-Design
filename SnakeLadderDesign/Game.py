class Game:

    def __init__(self, snake_ladder_board, player_manager):
        self.snake_ladder_board = snake_ladder_board
        self.player_manager = player_manager

    def start_game(self):
        while True:
            player = self.player_manager.get_player()
            die_roll = player.roll_die()
            new_pos = self.snake_ladder_board.get_final_position(player.pos, die_roll)
            player.pos = new_pos
            print(player.pos, player.user_name, die_roll)
            if new_pos == self.snake_ladder_board.size:
                return player





