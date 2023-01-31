import pygame, sys
from pygame.locals import*
pygame.init()
pygame.display.set_mode((400,400),RESIZABLE)      #click on the maximize button to see the full screen

game_running=True
while game_running:
    for event in pygame.event.get():
        if event.type==QUIT:            
            pygame.quit()
            sys.exit()
                                                # there's something wrong. we made a little change but that is not correctly appeared on the screen.
                                                #as we made the little change(resized the display) we have to update the display so that our little change
                                                #can appeare on the screen. ..check the next program..
