import pygame,sys
from pygame.locals import*
pygame.init()

screen_width=1000
screen_height=600
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("My game window")
images=[pygame.image.load('data/images/rose.jpg'),pygame.image.load('data/images/butterfly.jpg'),pygame.image.load('data/images/autumn.jpg')]
slideshow=0
def scale_image(n):
    w=images[n].get_width()
    h=images[n].get_height()

    if w>screen_width:
        if w>h:
            w_s=w-screen_width
            c=1/(w/w_s)
            w=screen_width
            h=h-int(h*c)
            images[n]=pygame.transform.scale(images[n],(w,h))
        if w<h:
            h_s=h-screen_height
            c=1/(h/h_s)
            h=screen_height
            w=w-int(w*c)
            images[n]=pygame.transform.scale(images[n],(w,h))

    if h>screen_height:
        h_s=h-screen_height
        c=1/(h/h_s)
        h=screen_height
        w=w-int(w*c)
        images[n]=pygame.transform.scale(images[n],(w,h))

game_running=True
while game_running:
    pygame.time.delay(1000)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

    scale_image(slideshow)
    screen.fill((0,0,0))
    screen.blit(images[slideshow],(0,0))
    if slideshow+1<=2:
        slideshow+=1
    else:
        slideshow=0
    pygame.display.update()
