import pygame,sys
from pygame.locals import*
from random import randint
pygame.init()

clock=pygame.time.Clock()
screen=pygame.display.set_mode((800,600))
color=(190, 200,144)


v1=randint(5,10)	#speed
v2=randint(5,10)

x1=50	#1st object position
y1=550

x2=740	#2nd object position
y2=550

n1=0
n2=9

sprite=[pygame.image.load('data/wheel/1.png'),pygame.image.load('data/wheel/2.png'),
pygame.image.load('data/wheel/3.png'),pygame.image.load('data/wheel/4.png'),pygame.image.load('data/wheel/5.png'),
pygame.image.load('data/wheel/6.png'),pygame.image.load('data/wheel/7.png'),pygame.image.load('data/wheel/8.png'),
pygame.image.load('data/wheel/9.png'),pygame.image.load('data/wheel/10.png')]

game_running=True
while game_running:
	clock.tick(60)

	x1+=v1
	x2-=v2
	if n1+1<10:
		n1+=1
	else:
		n1=0
	if n2-1>0:
		n2-=1
	else:
		n2=9
	if abs(x1-x2)<70:
		if v1>v2:
			v2=-v1
			n2=n1
		else:
			v1=-v2
			n1=n2

	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
		
	screen.fill(color)
	screen.blit(sprite[n1],(x1,y1)), screen.blit(sprite[n2],(x2,y2))
	pygame.display.update()
