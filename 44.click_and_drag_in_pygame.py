import pygame,sys
from pygame.locals import*
pygame.init()
clock = pygame.time.Clock()

screen=pygame.display.set_mode((1000,650))
screen_rect=screen.get_rect()
img=pygame.image.load('data/images/loneliness.jpg')  
img_rect=img.get_rect()

move=False
game_running=True
while game_running:
	clock.tick(60)
	for event in pygame.event.get():
		if event.type==QUIT:            
			pygame.quit()
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if img_rect.collidepoint(event.pos):
				move=True
				pygame.mouse.get_rel()
		elif event.type == pygame.MOUSEBUTTONUP:
			move=False
	screen.fill((255,255,255))

	if move==True:
		img_rect.move_ip(pygame.mouse.get_rel())
		img_rect.clamp_ip(screen_rect)
	screen.blit(img,(img_rect[0],img_rect[1]))
	pygame.display.update()
