import pygame,sys;
from pygame.locals import*
pygame.init()
clock=pygame.time.Clock()
width,height=800,600
screen=pygame.display.set_mode((width,height))
game_running=True
while game_running:
	caption=str(clock.get_fps())
	pygame.display.set_caption(caption)
	clock.tick(60)
	
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
	screen.fill("#87CEFA")
	pygame.display.update()
