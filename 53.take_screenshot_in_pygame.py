import pygame
import sys
from pygame.locals import *
import datetime
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((400, 400), RESIZABLE)


White = (255,255,255)
SeaGreen = (46, 139, 87)
Green = (0, 128, 0)

def draw_button(surface, text='button', font=None, font_color=White, bg_color=SeaGreen, position=(0, 0), size=(150, 40)):
	button_surface = pygame.Surface(size)
	button_surface.fill(bg_color)
	
	if font is None:
		font = pygame.font.Font(None, 22)
	text_render = font.render(text, True, font_color)
	text_rect = text_render.get_rect(center=(size[0] / 2, size[1] / 2))
	button_surface.blit(text_render, text_rect)
	
	rect = surface.blit(button_surface, position)
	
	return rect

game_running = True
while game_running:
	clock.tick(60)
	screen.fill(White)
	

	for i in range(1, 5):
		for j in range(1, 5):
			pygame.draw.rect(screen, SeaGreen, (i * 60, j * 60, 50, 50), border_radius=10)
			pygame.draw.rect(screen, Green, (i * 60, j * 60, 50, 50), 5, border_radius=10)
	

	button_rect = draw_button(screen, "Take Screenshot", position=(100, 320))


	pygame.display.update()
	

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == MOUSEBUTTONDOWN:
			mouse_pos = pygame.mouse.get_pos()
			if button_rect.collidepoint(mouse_pos):
				current_datetime = datetime.datetime.now()
				current_time = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
				#When the button clicked it will save the screenshot
				#pygame.image.save(screen, "screenshot.png")
				pygame.image.save(screen, f"screenshot_{current_time}.png") 

				#print("Screenshot saved as screenshot.png")
				print(f"Screenshot saved as screenshot_{current_time}.png")
	
