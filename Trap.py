#함정
import pygame

class Trap(pygame.Rect):
    screen = None
    trap = pygame.image.load("resources/images/trap.png")

    def __init__(self, screen, x ,y):
        super().__init__(self.trap.get_rect())
        self.screen = screen
        self.top = x
        self.left = y

    def draw(self):
        self.screen.blit(self.trap, (self.top, self.left))