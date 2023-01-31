#  Copyright 2021 Mahid
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY

import pygame,sys
from pygame.locals import*
pygame.init()
clock=pygame.time.Clock()

screen=pygame.display.set_mode((400,400))
red = (255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)

button_position=[
pygame.Rect(10,200,35,30),
pygame.Rect(50,200,35,30),
pygame.Rect(90,200,35,30),
pygame.Rect(130,200,35,30),
pygame.Rect(170,200,35,30),
pygame.Rect(10,250,35,30),
pygame.Rect(50,250,35,30),
pygame.Rect(90,250,35,30),
pygame.Rect(130,250,35,30),
pygame.Rect(170,250,35,30),
pygame.Rect(10,300,35,30),
pygame.Rect(50,300,35,30),
pygame.Rect(90,300,35,30),
pygame.Rect(130,300,35,30),
pygame.Rect(170,300,35,30),
pygame.Rect(10,350,35,30),
pygame.Rect(50,350,50,30),
pygame.Rect(115,350,70,30)]



def button(position_x=150,position_y=200,color=green,text='Button',b_w=35,b_h=30):
    pygame.draw.rect(screen,color, [position_x, position_y, b_w, b_h], border_radius=10)
    button_font=pygame.font.Font(pygame.font.get_default_font(), 20)
    button_text=button_font.render(text,True,white)
    screen.blit(button_text,(position_x+10,position_y+10))
def draw_button():
    button0=button(position_x=10,position_y=200,color=blue,text='0')
    button1=button(position_x=50,position_y=200,color=blue,text='1')
    button2=button(position_x=90,position_y=200,color=blue,text='2')
    button3=button(position_x=130,position_y=200,color=blue,text='3')
    button4=button(position_x=170,position_y=200,color=blue,text='4')
    button5=button(position_x=10,position_y=250,color=blue,text='5')
    button6=button(position_x=50,position_y=250,color=blue,text='6')
    button7=button(position_x=90,position_y=250,color=blue,text='7')
    button8=button(position_x=130,position_y=250,color=blue,text='8')
    button9=button(position_x=170,position_y=250,color=blue,text='9')
    

    button_plus= button(position_x=10,position_y=300,color=blue,text='+')
    button_minus= button(position_x=50,position_y=300,color=blue,text='-')
    button_multiplication= button(position_x=90,position_y=300,color=blue,text='x')
    button_division= button(position_x=130,position_y=300,color=blue,text='/')

    button_equal=button(position_x=170,position_y=300,color=blue,text='=')

    button_dot=button(position_x=10,position_y=350,color=blue,text='.')
    button_delete=button(position_x=50,position_y=350,color=blue,text='del',b_w=50)
    button_clear=button(position_x=115,position_y=350,color=blue,text='clear',b_w=70)

    
    
message=''
x_i=''
game_running=True
while game_running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

        mouse_position=pygame.mouse.get_pos()
        if event.type==pygame.MOUSEBUTTONDOWN:
            for i in range(len(button_position)):
                if button_position[i].collidepoint(mouse_position):
                    if event.button==1:
                        message=''
                        if i==17:
                            x_i=''
                        elif i==14:
                            
                            x_i=x_i

                            
                            z=['+','-','*','/']
                            n=[]

                            le=len(x_i)
                            for i in range(le):
                                if x_i[i] in z:
                                    n.append(x_i[i])
                            
                                    
                            nw=x_i
                            l=len(n)
                            for i in range(l):
                                nw=nw.replace(n[i],'n')          
                            new=nw.split('n')
                            o=[]
                            for item in new:
                                item=float(item)
                                o.append(str(item))
                            x_i2=o[0]
                            for i in range(len(n)):
                                x_i2=x_i2+n[i]+o[i+1]

                            try:
                                x_i=str(eval(x_i2))
                            except:
                                message='Error'
                        elif i==10:
                            x_i=x_i+'+'
                        elif i==11:
                            x_i=x_i+'-'
                        elif i==12:
                            x_i=x_i+'*'
                        elif i==13:
                            x_i=x_i+'/'
                        elif i==15:
                            x_i=x_i+'.'
                        elif i==16:
                            x_i=x_i[:-1]
                        else:
                            x_i=x_i+str(i)
    screen.fill(white)
    draw_button()
    button(position_x=10,position_y=20,text=x_i, b_w=300)
    button(position_x=10,position_y=50,color=red,text=message, b_w=300)
    pygame.display.update()
