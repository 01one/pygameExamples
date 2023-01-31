import pygame,sys
from pygame.locals import*
pygame.init()
screen=pygame.display.set_mode((400,400),RESIZABLE)
pygame.display.set_caption("My game window")
image=pygame.image.load('data/images/icon.png')
pygame.display.set_icon(image)                          #set the icon

game_running=True
while game_running:
	for event in pygame.event.get():
		if event.type==QUIT:            
			pygame.quit()
			sys.exit()
	pygame.display.update()
