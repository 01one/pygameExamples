import pygame,sys
from pygame.locals import*
pygame.init()
screen=pygame.display.set_mode((400,400))
text=''
white=(255,255,255)
black=(0,0,0)
def update_time():
    time_font=pygame.font.Font(pygame.font.get_default_font(), 20)
    time_text=time_font.render(text,True,white)
    screen.blit(time_text,(50,50))

game_running=True
while game_running:
    for event in pygame.event.get():
        if event.type==QUIT:            
            pygame.quit()
            sys.exit()
    
    time_passed=pygame.time.get_ticks() #time passed from init
    time_passed_second=time_passed/1000
    text=str(time_passed_second)
    screen.fill(black)
    update_time()
    pygame.display.update()
