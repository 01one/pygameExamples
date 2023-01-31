import pygame,sys
from pygame.locals import*
pygame.init()

clock=pygame.time.Clock()
screen=pygame.display.set_mode((800,600))
color=(190, 200,144)

velocity_x=10
velocity_y=3
x=0
y=50

sprite=pygame.image.load('data/wheel/1.png')
game_running=True
while game_running:
	clock.tick(60)
	x+=velocity_x
	y+=velocity_y
	velocity_x-=.1
	velocity_y+=.2
	if velocity_x<0:
		velocity_x=velocity_x+.1	

	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
	
	screen.fill(color)
	screen.blit(sprite,(x,y))
	pygame.display.update()
