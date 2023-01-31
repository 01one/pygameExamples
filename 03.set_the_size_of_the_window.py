import pygame, sys
from pygame.locals import*
pygame.init()
pygame.display.set_mode((400,400))      #pygame.display.set_mode((width,height))   #width height in pixel

game_running=True
while game_running:
    for event in pygame.event.get():
        if event.type==QUIT:            
            pygame.quit()
            sys.exit()
