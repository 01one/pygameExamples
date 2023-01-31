import pygame,sys
from pygame.locals import*
pygame.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode((400,400))
lightgreen=(144, 238,144)

x=50
y=300
m=1
v=10
jump=0

sprite=pygame.image.load('data/wheel/1.png')
game_running=True
while game_running:
	clock.tick(60)
	pygame.time.delay(20)
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
			
	keys = pygame.key.get_pressed()
	if jump==0:
		if keys[pygame.K_SPACE]:
			jump =1
	if jump==1 :
		k =.5*m*v**2
		y-= k
		v-=1
		if v<0:
			m =-1
		if v ==-11:
			m=1
			v=10
			jump=0
			
	screen.fill(lightgreen)
	screen.blit(sprite,(x,y))
	pygame.display.update()
