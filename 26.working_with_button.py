import pygame,sys
from pygame.locals import*
pygame.init()
clock=pygame.time.Clock()


screen=pygame.display.set_mode((800,600))
background=(255,255,255)
purple=(187,51,255)
apple_green=(170,204,0)
cornflower_blue=(128,149,255)
button_color=cornflower_blue
button_position=pygame.Rect(50,50,100,50)

game_running=True
while game_running:
	clock.tick(60)
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()


	mouse_position=pygame.mouse.get_pos()
	if event.type==pygame.MOUSEMOTION:
		if button_position.collidepoint(mouse_position):
			button_color=purple
		else:
			button_color=cornflower_blue


	if event.type==pygame.MOUSEBUTTONDOWN:
		if button_position.collidepoint(mouse_position):
			if event.button==1:
				button_color=apple_green

		
	screen.fill(background)
	pygame.draw.rect(screen,(button_color),(button_position))
	pygame.display.update()
