import pygame,sys
from pygame.locals import*
pygame.init()
clock=pygame.time.Clock()

screen=pygame.display.set_mode((400,400),RESIZABLE)
lightgreen=(144, 238,144)
x=50
y=300
width=50
height=50

sprite=[pygame.image.load('data/wheel/1.png'),pygame.image.load('data/wheel/2.png'),
pygame.image.load('data/wheel/3.png'),pygame.image.load('data/wheel/4.png'),pygame.image.load('data/wheel/5.png'),
pygame.image.load('data/wheel/6.png'),pygame.image.load('data/wheel/7.png'),pygame.image.load('data/wheel/8.png'),
pygame.image.load('data/wheel/9.png'),pygame.image.load('data/wheel/10.png')]

n=9


game_running=True
while game_running:
	clock.tick(60)
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
			
	keys = pygame.key.get_pressed()
	if keys[pygame.K_UP]:
		y-=5
		n=0
	elif keys[pygame.K_DOWN]:
		y+=5
		n=0
	elif keys[pygame.K_LEFT]:
		x-=5
		n-=1
		if n<0:
			n=9
	elif keys[pygame.K_RIGHT]:
		x+=5
		n+=1
		if n>9:
			n=0
	screen.fill(lightgreen)
	screen.blit(sprite[n],(x,y))
	pygame.display.update()
