from game import Game
from board import Board
size = (20, 50) # 20x50
prob = 0.1
board = Board(size, prob)
screen_size = (1400, 800) # 1400x800
game = Game(board, screen_size)
game.run()
