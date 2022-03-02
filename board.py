from piece import Piece
from random import random

class Board():
    def __init__(self, size, prob):
        self.size = size
        self.prob = prob
        self.lost = False
        self.won = False
        self.num_clicked = 0
        self.num_non_bombs = 0
        self.set_board()
        
        
    def set_board(self):
        self.board = []
        for row in range(self.size[0]):
            row = []
            for col in range(self.size[1]):
                has_bomb = random() < self.prob
                if not has_bomb:
                    self.num_non_bombs += 1
                piece = Piece(has_bomb)
                row.append(piece)
            self.board.append(row)
        self.set_neighbors()
        
    def set_neighbors(self):
        for row in range(self.size[0]):
             for col in range(self.size[1]):
                 piece = self.get_piece((row, col))
                 neighbors = self.get_list_of_neighbors((row, col))
                 piece.set_neighbors(neighbors)
                 
    def get_list_of_neighbors(self, index):
        neighbors = []
        for row in range(index[0] - 1, index[0] + 2):
            for col in range(index[1] - 1, index[1] + 2):
                out_of_bounds = row < 0 or row >= self.size[0] or col < 0 or col >= self.size[1]
                same = row == index[0] and col == index[1]
                if same or out_of_bounds:
                    continue
                neighbors.append(self.get_piece((row, col)))
        return neighbors
            
    def get_size(self):
        return self.size
    
    def get_piece(self, index):
        return self.board[index[0]][index[1]]
    
    def handle_click(self, piece, flag):
        if self.num_clicked == 0 and piece.get_has_bomb():
            piece.set_has_bomb(False)
            if not self.board[0][0].get_has_bomb():
                self.board[0][0].set_has_bomb(True)
            elif not self.board[0][1].get_has_bomb():
                self.board[0][1].set_has_bomb(True)
            else:
                self.board[0][2].set_has_bomb(True)
        if piece.get_clicked():
            piece.set_num_flags()
            if piece.get_num_flags() == piece.get_num_around() and piece.get_num_around() != 0:
                for neighbor in piece.get_neighbors():
                    if neighbor.get_clicked() or neighbor.get_flagged():
                        pass
                    else:
                        neighbor.click()
                        self.num_clicked += 1
                        if (neighbor.get_has_bomb()):
                            self.lost = True
                            return
        if piece.get_clicked() or (not flag and piece.get_flagged()):
            return 
        if flag:
            piece.toggle_flag()
            return
        piece.click()
        if (piece.get_has_bomb()):
            self.lost = True
            return
        self.num_clicked += 1
        if piece.get_num_around() != 0:
            return
        if piece.get_num_around() == 0:
            for neighbor in piece.get_neighbors():
                self.handle_click(neighbor, False)
    
    def get_lost(self):
        return self.lost
        
    def get_won(self):
        return self.num_non_bombs == self.num_clicked
        