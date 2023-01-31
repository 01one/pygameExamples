import pygame,sys
from pygame.locals import*
from random import randint

pygame.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode((800,600))
lightgreen=(144, 238,144)

v=0
v1=9.8 
x=0
y=0
u=1

x=randint(50,500)
y=randint(50,80)


sprite=pygame.image.load('data/wheel/1.png')
game_running=True
while game_running:
    clock.tick(60)      

    for event in pygame.event.get():
        if event.type==QUIT:            
            pygame.quit()
            sys.exit()
    if y+v<540 and u==1:
        y+=v
        v+=.5
    if y+v>540:
        u=0
        v=0

    if y-v1>0 and u==0:
        y-=v1 
        v1-=.1
    if v1-.5<0:
        u=1
        v1=9.8
    screen.fill(lightgreen)
    screen.blit(sprite,(x,y))
    pygame.display.update()
