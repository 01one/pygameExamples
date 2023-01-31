#use LEFT or RIGHT button
import pygame,sys
from pygame.locals import*
pygame.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode((400,400))
lightgreen=(144, 238,144)

a=-.1
x=50
y=300
velocity=7
new_v=velocity+a

sprite=[pygame.image.load('data/wheel/1.png'),pygame.image.load('data/wheel/2.png'),
pygame.image.load('data/wheel/3.png'),pygame.image.load('data/wheel/4.png'),pygame.image.load('data/wheel/5.png'),
pygame.image.load('data/wheel/6.png'),pygame.image.load('data/wheel/7.png'),pygame.image.load('data/wheel/8.png'),
pygame.image.load('data/wheel/9.png'),pygame.image.load('data/wheel/10.png')]

n=0
game_running=True
while game_running:
    clock.tick(60)      
    for event in pygame.event.get():
        if event.type==QUIT:            
            pygame.quit()
            sys.exit()
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_RIGHT:
            new_v=velocity+a
            if x+velocity<340:                #the display width=400px
                x+=velocity
            else:
                x=x
            n+=1
            if n>9:
                n=0

        elif event.key==pygame.K_LEFT:
            new_v=velocity+a
            if x-velocity>0:
                x-=velocity
            else:
                x=x
            n-=1
            if n<0:
                n=9

    if event.type==pygame.KEYUP:
        if event.key==pygame.K_RIGHT:
            if x+new_v+a<340 and new_v+a>0:
                new_v=new_v+a
                x+=new_v
                n=9
        elif event.key==pygame.K_LEFT:
            if x-new_v+a>0 and new_v+a>0:
                new_v=new_v+a
                x-=new_v
                n=5
    screen.fill(lightgreen)
    screen.blit(sprite[n],(x,y))
    pygame.display.update()
