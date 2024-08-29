

class Game:
    PLAYER1 = 0
    PLAYER2 = 1
    player_to_move_map = {
        PLAYER1: 'X',
        PLAYER2: 'O'
    }

    def __init__(self, board, player1, player2):
        self.board = board
        self.players = [player1, player2]
        self.player_turn = 0
        self.has_ended = False

    def make_move(self,x,y):
        if self.board.populate_cell(x, y, self.player_to_move_map[self.player_turn]):
            self.player_turn = 1-self.player_turn
            print("Your move has been made")
            game_ended, player = self.has_game_ended()
            if game_ended and player:
                print(f"Game has ended, {player.name} is the Winner")
            elif game_ended:
                print("Game drawn")
        else:
            print('Invalid move')

        self.board.print_board()

    def has_game_ended(self):
        self.has_ended = True
        if self.board.check_rows('X') or  self.board.check_column('X') or self.board.check_diagonal('X'):
            return True, self.players[0]
        elif self.board.check_rows('O') or self.board.check_column('O') or self.board.check_diagonal('O'):
            return True, self.players[1]
        if self.board.all_cells_filled():
            return True, None
        return False, None
