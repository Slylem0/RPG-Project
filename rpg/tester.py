import pygame, sys
import utilities, cosa, personaje, escenario
from pygame.locals import *




def main():
    screen = pygame.display.set_mode((utilities.WIDTH, utilities.HEIGHT))
    pygame.display.set_caption("Pruebas Pygame")
    clock = pygame.time.Clock() 
    monigote = personaje.Personaje(["img/elfafront1.png", "img/elfafront2.png", "img/elfafront3.png", "img/elfafront4.png"],
    ["img/elfaback1.png", "img/elfaback2.png", "img/elfaback3.png", "img/elfaback4.png"],
    ["img/elfaizq1.png", "img/elfaizq2.png", "img/elfaizq3.png", "img/elfaizq4.png"],
    ["img/elfader1.png", "img/elfader2.png", "img/elfader3.png", "img/elfader4.png"],
    utilities.WIDTH/2, utilities.HEIGHT/2)
    arbol = cosa.Cosa("img/arbolimg1.png", 20, 100)
    arbol1 = cosa.Cosa("img/arbolimg1.png", 140, 100)
    esc = escenario.Escenario("background.jpg")
    esc.objetos.add(arbol)
    esc.objetos.add(arbol1)
    esc.personajes.add(monigote)
    while 1:
        time = clock.tick(30)
        keys = pygame.key.get_pressed()
        if keys[K_q]: sys.exit(0)
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
        for i in esc.personajes:
            i.mover(keys, time, esc.objetos)
        
        screen.blit(esc.backgroundImage, (0,0))
        for i in esc.objetos:
            screen.blit(i.image, i.rect)
        for i in esc.personajes:
            screen.blit(i.image, i.rect)
        pygame.display.flip() 
        
        
    return 0

if __name__ == '__main__':
    pygame.init()
    main()