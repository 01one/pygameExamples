import pygame,sys
from pygame.locals import*
pygame.init()
screen=pygame.display.set_mode((400,400),RESIZABLE)

game_running=True
while game_running:
    for event in pygame.event.get():
        if event.type==QUIT:            
            pygame.quit()
            sys.exit()
    pygame.draw.circle(screen,(255,100,255),(100,100),20,2)             #circle(surface,color,position,radius,thickness)
    pygame.display.update()
