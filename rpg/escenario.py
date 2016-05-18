import pygame, utilities


class Escenario():
    
    def __init__(self, backgroundDir):
        self.backgroundImage = utilities.load_image(backgroundDir)
        self.objetos = pygame.sprite.Group()
        self.personajes = pygame.sprite.Group()