from game import Game
from board import Board
size = (20, 50)
prob = 0.2
board = Board(size, prob)
screen_size = (1400, 800)
game = Game(board, screen_size)
game.run()
