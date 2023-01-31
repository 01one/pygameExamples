import pygame,sys
from pygame.locals import*
pygame.init()
screen=pygame.display.set_mode((400,400),RESIZABLE)
pygame.display.set_caption("My game window")
image=pygame.image.load('data/images/autumn.jpg')       #load the image

game_running=True
while game_running:
	for event in pygame.event.get():
		if event.type==QUIT:            
			pygame.quit()
			sys.exit()
	screen.blit(image,(0,0))                            #draw the image on screen
	pygame.display.update()
