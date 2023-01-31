import pygame,sys
from pygame.locals import*
pygame.init()
clock=pygame.time.Clock()


screen=pygame.display.set_mode((800,600))
background=(255,255,255)
black=(0,0,0)


font=pygame.font.Font('data/font/VT323-Regular.ttf', 70)
text=font.render('Coding is poetry',True,black)


game_running=True
while game_running:
	clock.tick(60)
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()

		
	screen.fill(background)
	screen.blit(text,(100,100))
	pygame.display.update()
