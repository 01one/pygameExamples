import pygame,sys
from pygame.locals import*
pygame.init()

screen=pygame.display.set_mode((400,400))
red = (255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)


def button(position_x=150,position_y=200,color=green,text='Button'):
    pygame.draw.rect(screen,color, [position_x, position_y, 80, 40], border_radius=10)
    button_font=pygame.font.Font(pygame.font.get_default_font(), 20)
    button_text=button_font.render(text,True,white)
    screen.blit(button_text,(position_x+10,position_y+10))

game_running=True
while game_running:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(white)
    button1=button(position_y=50,color=blue,text='Menu')
    button2=button(position_y=100,color=red,text='Start')
    button3=button(position_y=150,color=green,text='Exit')
    pygame.display.update()
