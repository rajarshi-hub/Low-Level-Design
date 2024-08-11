from Board import Board
from Game import Game
from PlayerManager import PlayerManager
from Player import Player


player1 = Player("Rajarshi")
player2 = Player("Pawan")
player3 = Player("Raghu")
player_manger = PlayerManager([player1, player2, player3])
board = Board(
    [
        (2,54),
        (7, 32),
        (56,78),
        (45, 23),
        (98, 6),
        (94, 54),
        (45, 76),
        (32, 86)
    ],
    100
)
game = Game(board, player_manger)
print(game.start_game().user_name, '**********')

