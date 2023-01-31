import pygame,sys
from pygame.locals import*
pygame.init()

clock=pygame.time.Clock()
screen=pygame.display.set_mode((800,600))
color=(144, 238,144)

game_running=True
while game_running:
	clock.tick(60)
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
	screen.fill(color)
	pygame.display.update()
