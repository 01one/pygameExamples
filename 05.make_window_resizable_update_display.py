import pygame, sys
from pygame.locals import*
pygame.init()
pygame.display.set_mode((400,400),RESIZABLE)    #click on the maximize button to see the full screen

game_running=True
while game_running:
    for event in pygame.event.get():
        if event.type==QUIT:            
            pygame.quit()
            sys.exit()
    pygame.display.update()                     # now the display 'll continuosly update until the game exit.
