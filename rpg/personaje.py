import pygame, utilities
from pygame.locals import *


# -------- Constantes ----------------------------------------------------------

# ------------------------------------------------------------------------------

class Personaje(pygame.sprite.Sprite, pygame.Rect):
    
    def __init__(self, front, back, left, right, x, y):
        # Llamo al constructor de la super clase
        pygame.sprite.Sprite.__init__(self)
        
        self.frontImages = front
        self.backImages = back
        self.rightImages = right
        self.leftImages = left
        self.speed = 0.1
        self.image = utilities.load_image(self.frontImages[0], True)
        self.imgItem = 0
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
    
    def mover(self, keys, time, objetos):
        # Mueve para arriba
        if self.rect.top >= 0: 
            if keys[K_UP]:
                self.rect.centery -= self.speed * time
                if self.imgItem == 4: self.imgItem = 0
                self.image = utilities.load_image(self.backImages[self.imgItem], True)
                self.imgItem += 1
                
        # Mueve para abajo
        if self.rect.bottom <= utilities.HEIGHT: 
            if keys[K_DOWN]:
                self.rect.centery += self.speed * time
                if self.imgItem == 4: self.imgItem = 0
                self.image = utilities.load_image(self.frontImages[self.imgItem], True)
                self.imgItem += 1
        # Mueve para la derecha
        if self.rect.right <= utilities.WIDTH:
            if keys[K_RIGHT]:
                self.rect.centerx += self.speed * time
                if self.imgItem == 4: self.imgItem = 0
                self.image = utilities.load_image(self.rightImages[self.imgItem], True)
                self.imgItem += 1
        # Mueve para la izquierda        
        if self.rect.left >= 0:
            if keys[K_LEFT]:
                self.rect.centerx -= self.speed * time
                if self.imgItem == 4: self.imgItem = 0
                self.image = utilities.load_image(self.leftImages[self.imgItem], True)
                self.imgItem += 1
                
        lista_impactos = pygame.sprite.spritecollide(self, objetos, False)
        
        for c in lista_impactos:
            #Si nos estamos desplazando hacia la derecha, hacemos que nuestro lado derecho sea el lado izquierdo del objeto que hemos tocado-
            if keys[K_RIGHT]:
                self.rect.right = c.rect.left
                continue
            elif keys[K_LEFT]:
                # En caso contrario, si nos desplazamos hacia la izquierda, hacemos lo opuesto.
                self.rect.left = c.rect.right
                continue
            if keys[K_UP]:
                self.rect.top = c.rect.bottom
                continue 
            elif keys[K_DOWN]:
                self.rect.bottom = c.rect.top
                continue   
       
        
        # Reseteamos nuestra posicion basandonos en la parte superior/inferior del objeto.
            
              
             
                