from Board import Board

from Game import Game
from Player import Player

board = Board()
player1 = Player("Raj", 1)
player2 = Player("Manish", 2)
game = Game(board, player1, player2)
game.make_move(0,0)
game.make_move(2,2)
game.make_move(0,1)
game.make_move(0,2)
game.make_move(1,1)
game.make_move(2,1)
game.make_move(1,2)
game.make_move(1,0)
game.make_move(2,0)

