import datetime
import pygame,sys
from pygame.locals import*
pygame.init()


clock=pygame.time.Clock()

screen=pygame.display.set_mode((800,600))

clock_font=pygame.font.Font(pygame.font.get_default_font(), 150)



game_running=True
while game_running:
	# It will run 1 frame per second. So the time will update every second
	clock.tick(1)
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
	current_time = datetime.datetime.now()

	hour = current_time.hour
	minute = current_time.minute
	second = current_time.second

	clock_time = f"{hour:02}:{minute:02}:{second:02}"
	screen.fill((255,255,255))
	clock_text=clock_font.render(clock_time,True,(0,0,0))
	screen.blit(clock_text,(100,200))
	pygame.display.update()
