from multiprocessing import Process, Value
import time
import pygame,sys
from pygame.locals import*
pygame.init()

def number(n):
	for i in range(22):
		n.value=i
		print('********************************************')
		time.sleep(.05)
def graphical_presentation(n):
	screen=pygame.display.set_mode((400,400))
	game_running=True
	while game_running:
		for event in pygame.event.get():
			if event.type==QUIT:            
				pygame.quit()
				sys.exit()
		screen.fill((255,255,255))
		pygame.draw.rect(screen,(200,200,100),(200,200,50,40),2)
		pygame.display.update()
		x=n.value
		if x<21:
			print(x)
if __name__ == '__main__':	
	num = Value('i',0)
	process1=Process(target=number,args=[num])
	process2=Process(target=graphical_presentation,args=[num])
	process1.start()
	process2.start()
	process1.join()
	process2.join()
