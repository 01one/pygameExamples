import pygame,sys
from pygame.locals import*
pygame.init()
clock=pygame.time.Clock()
white=(255,255,255)
black=(0,0,0)

screen_width=640
screen_height=480
screen=pygame.display.set_mode((screen_width,screen_height),RESIZABLE|SCALED)

game_running=True
while game_running:
	clock.tick(30)
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
	screen.fill(white)
	pygame.draw.rect(screen,(84,42,168),(200,200,600,300),border_radius=50)
	pygame.draw.circle(screen,(255,100,255),(100,100),40)
	pygame.display.update()
