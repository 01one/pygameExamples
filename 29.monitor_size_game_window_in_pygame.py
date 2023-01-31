import pygame,sys
from pygame.locals import*
pygame.init()
user_display=pygame.display.Info()
width,height=user_display.current_w,user_display.current_h
screen=pygame.display.set_mode((width,height))

background=(255,255,255)
red=(255,0,0)
cornflower_blue=(128,149,255)
button_color=cornflower_blue
button_position=pygame.Rect(width/2,100,80,40)

def button():
	pygame.draw.rect(screen,button_color, [width/2, 100, 80, 40], border_radius=10)
	button_font=pygame.font.Font(pygame.font.get_default_font(), 20)
	button_text=button_font.render('Exit',True,background)
	pygame.draw.rect(screen,button_color, [width/2, 100, 80, 40], border_radius=10)
	screen.blit(button_text,(width/2+20,110))


game_running=True
while game_running:
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
	mouse_position=pygame.mouse.get_pos()
	if event.type==pygame.MOUSEMOTION:
		if button_position.collidepoint(mouse_position):
			button_color=red
		else:
			button_color=cornflower_blue
			
	if event.type==pygame.MOUSEBUTTONDOWN:
		if button_position.collidepoint(mouse_position):
			if event.button==1:
				pygame.quit()
				sys.exit()
	screen.fill(background)
	button()
	pygame.display.update()
