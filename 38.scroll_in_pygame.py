import pygame,sys
from pygame.locals import*
pygame.init()
clock=pygame.time.Clock()
screen_width=300
screen_height=300
screen=pygame.display.set_mode((screen_width,screen_height))
white=(255,255,255)
black=(0,0,0)

def text_view(text_color,text,text_font,text_rect):
    text_lines = []
    splited_lines =text.splitlines()
    for splited_line in splited_lines:
        if text_font.size(splited_line)[0] > text_rect.width:
            words = splited_line.split(' ')
            for word in words:
                if text_font.size(word)[0] >= text_rect.width:
                    pass
            fitted_line = ""
            for word in words:
                test_line = fitted_line + word + " "  
                if text_font.size(test_line)[0] < text_rect.width:
                    fitted_line = test_line
                else:
                    text_lines.append(fitted_line)
                    fitted_line = word + " "
            text_lines.append(fitted_line)
        else:
            text_lines.append(splited_line)
    surface = pygame.Surface(text_rect.size)
    surface.fill(white)
    text_raw = 0
    for line in text_lines:
        if text_raw + text_font.size(line)[1] >= text_rect.height:
            pass
        if line != "":
            text_surface = text_font.render(line, 1, text_color)
            surface.blit(text_surface, (0, text_raw))
        text_raw +=text_font.size(line)[1]
    return surface
    
scroll=0

game_running=True
while game_running:
	clock.tick(60)
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
		if event.type == MOUSEWHEEL:
			if event.y<0:
				scroll-=20
			elif event.y>0:
				scroll+=20

			
	Text_color=black
	Text="Twinkle, Twinkle, Little Star\nBY JANE TAYLOR\n\nTwinkle, twinkle, little star,\nHow I wonder what you are!\nUp above the world so high,\nLike a diamond in the sky.\n\nWhen the blazing sun is gone,\nWhen he nothing shines upon,\nThen you show your little light,\nTwinkle, twinkle, all the night.\n\nThen the traveler in the dark\nThanks you for your tiny spark,\nHow could he see where to go,\nIf you did not twinkle so?\nIn the dark blue sky you keep,\nOften through my curtains peep\nFor you never shut your eye,\nTill the sun is in the sky.\n\nAs your bright and tiny sparkn\nLights the traveler in the dark,\nThough I know not what you are,\nTwinkle, twinkle, little star."
	Text_font=pygame.font.Font('data/font/VT323-Regular.ttf', 20)
	Text_rect=pygame.Rect(10,scroll,screen_width,500)
	show_text=text_view(Text_color,Text,Text_font,Text_rect)

	screen.fill(white)
	screen.blit(show_text, Text_rect)
	pygame.display.update()
