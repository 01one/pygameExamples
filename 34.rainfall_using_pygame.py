#  Copyright 2021 Mahid
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY
import pygame,sys
from pygame.locals import*
from random import randint

pygame.init()
clock=pygame.time.Clock()

width=640
height=426
screen=pygame.display.set_mode((width,height))
image=pygame.image.load('data/images/loneliness.jpg')

class Rainfall():
	def __init__(self):
		self.x=randint(1,width)
		self.y=randint(-height,height)
	
	def show(self):
		pygame.draw.line(screen,((255,255,255)),(self.x,self.y),(self.x,self.y+.5),1)
		
	def update(self):
		if self.y>height:
			self.y=randint(-10,0)

		else:
			self.y=10+self.y*1.03
n=1
Rain=[Rainfall() for i in range(1000)]
game_running=True
while game_running:
	clock.tick(60)
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
	screen.blit(image,(0,0))
	
	
	for i in range(n):
		Rain[i].show()
		Rain[i].update()
	if n+1<1000:
		n+=1
	pygame.display.update()
