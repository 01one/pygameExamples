import pygame,sys
from pygame.locals import*
pygame.init()

screen=pygame.display.set_mode((400,400),RESIZABLE)
lightgreen=(144, 238,144)
x_coordinates=50
y_coordinates=50
width=50
height=50

game_running=True
while game_running:
    for event in pygame.event.get():
        if event.type==QUIT:            
            pygame.quit()
            sys.exit()

        elif event.type==pygame.KEYDOWN:        #keyboard events
            if event.key==pygame.K_w:
                y_coordinates-=5
            elif event.key==pygame.K_s:
                y_coordinates+=5
            elif event.key==pygame.K_a:
                x_coordinates-=5
            elif event.key==pygame.K_d:
                x_coordinates+=5

    screen.fill(lightgreen)
    pygame.draw.rect(screen,(255,255,255),(x_coordinates,y_coordinates,height,width))
    pygame.display.update()
