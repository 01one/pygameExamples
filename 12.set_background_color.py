import pygame,sys
from pygame.locals import*
pygame.init()
screen=pygame.display.set_mode((400,400),RESIZABLE)
lightgreen=(144, 238,144)
game_running=True
while game_running:
    for event in pygame.event.get():
        if event.type==QUIT:            
            pygame.quit()
            sys.exit()
    screen.fill(lightgreen)
    pygame.display.update()
