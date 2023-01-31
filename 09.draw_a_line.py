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
    pygame.draw.line(screen,((255,255,255)),(50,50),(50,200),5)            #line(surface, color, start_position, end_positon, thickness)
    pygame.display.update()
