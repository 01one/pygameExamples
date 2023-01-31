import pygame,sys                           #import necessary module
from pygame.locals import*
pygame.init()                               #initialize imported pygame modules
pygame.display.set_mode((400,400))

game_running=True
while game_running:                         #game loop keeps the game running until you exit the game.
    for event in pygame.event.get():
        if event.type==QUIT:            
            pygame.quit()
            sys.exit()
