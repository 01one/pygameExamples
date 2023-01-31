import pygame,sys
from pygame.locals import*
pygame.init()
pygame.display.set_mode((400,400),RESIZABLE)
pygame.display.set_caption("My game window")        #pygame.display.set_caption("your program title")

game_running=True
while game_running:
    for event in pygame.event.get():
        if event.type==QUIT:            
            pygame.quit()
            sys.exit()
    pygame.display.update()
