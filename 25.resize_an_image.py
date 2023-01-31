import pygame,sys
from pygame.locals import*
pygame.init()

screen=pygame.display.set_mode((800,600))
color=(190, 200,144)

sprite=pygame.image.load('data/wheel/1.png')
sprite=pygame.transform.scale(sprite,(256,256))

game_running=True
while game_running:
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
		
	screen.fill(color)
	screen.blit(sprite,(50,300))
	pygame.display.update()
