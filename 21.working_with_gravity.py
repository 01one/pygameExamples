import pygame,sys
from pygame.locals import*
from random import randint

pygame.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode((800,600))
lightgreen=(144, 238,144)

a=9.8
x=0
y=0

x=randint(50,500)
y=randint(50,80)


sprite=pygame.image.load('data/wheel/1.png')

n=0
game_running=True
while game_running:
    #pygame.time.delay(1000)
    clock.tick(60)      

    for event in pygame.event.get():
        if event.type==QUIT:            
            pygame.quit()
            sys.exit()
    if y+9.8<540:
        y+=9.8

    screen.fill(lightgreen)
    screen.blit(sprite,(x,y))
    pygame.display.update()
