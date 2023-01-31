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
    pygame.draw.rect(screen,(200,200,100),(200,200,50,40),2)            #rect(surface,color,(x,y,height,width)
    pygame.display.update()
