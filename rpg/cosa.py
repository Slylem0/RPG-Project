import pygame, utilities
from pygame.locals import *

class Cosa (pygame.sprite.Sprite):
    
    def __init__(self, imageDir, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = utilities.load_image(imageDir, True)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
