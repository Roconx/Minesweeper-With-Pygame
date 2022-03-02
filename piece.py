class Piece():
    def __init__(self, has_bomb):
        self.has_bomb = has_bomb
        self.clicked = False
        self.flagged = False
        
    def get_has_bomb(self):
        return self.has_bomb
    
    def set_has_bomb(self, value):
        self.has_bomb = value
    
    def get_clicked(self):
        return self.clicked
    
    def set_neighbors(self, neighbors):
        self.neighbors = neighbors
        self.set_num_around()
        self.set_num_flags()

        
    def set_num_around(self):
        self.num_around = 0
        for piece in self.neighbors:
            if (piece.get_has_bomb()):
                self.num_around += 1
                
    def get_num_around(self):
        return self.num_around
                
    def set_num_flags(self):
        self.num_flags = 0
        for piece in self.neighbors:
            if (piece.get_flagged()):
                self.num_flags += 1
                
    def get_num_flags(self):
        return self.num_flags
    
    def get_flagged(self):
        return self.flagged
    
    def toggle_flag(self):
        self.flagged = not self.flagged
        
    def click(self):
        self.clicked = True
        
    def get_neighbors(self):
        return self.neighbors