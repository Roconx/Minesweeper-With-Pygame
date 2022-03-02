from turtle import position
import pygame
import os
from time import sleep

class Game():
    def __init__(self, board, screen_size):
        self.board = board
        self.screen_size = screen_size
        self.piece_size = self.screen_size[0] // self.board.get_size()[1], self.screen_size[1] // self.board.get_size()[0]
        pygame.init()
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Minesweeper")
        self.load_images()

        
    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            clock.tick(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    right_click = pygame.mouse.get_pressed()[2]
                    self.handle_click(position, right_click)
            self.draw()
            pygame.display.flip()
            if self.board.get_won():
                sound = pygame.mixer.Sound("win.wav")
                sound.play()
                sleep(3)
                running = False
            if self.board.get_lost():
                running = False
            
        pygame.quit()
        
    def draw(self):
        top_left = (0, 0)
        for row in range(self.board.get_size()[0]):
            for col in range(self.board.get_size()[1]):
                piece = self.board.get_piece((row, col))
                image = self.get_image(piece)
                self.screen.blit(image, top_left)
                top_left = top_left[0] + self.piece_size[0], top_left[1]
            top_left = 0, top_left[1] + self.piece_size[1]
    
    def load_images(self):
        self.images = {}
        for file_name in os.listdir("images"):
            if not file_name.endswith(".png"):
                continue
            image = pygame.image.load(f"images/{file_name}").convert()
            image = pygame.transform.scale(image, self.piece_size).convert()
            self.images[file_name.split(".")[0]] = image
            
    def get_image(self, piece):
        string = None
        if (piece.get_clicked()):
            string = "bomb-at-clicked-block" if piece.get_has_bomb() else str(piece.get_num_around())
        else:
            string = "flag" if piece.get_flagged() else "empty-block"
        return self.images[string]
    
    def handle_click(self, position, right_click):
        index = position[1] // self.piece_size[1], position[0] // self.piece_size[0]
        piece = self.board.get_piece(index)
        self.board.handle_click(piece, right_click)