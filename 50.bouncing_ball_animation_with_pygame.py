import pygame,sys,random
from pygame.locals import*
pygame.init()
clock=pygame.time.Clock()
display_x=600
display_y=600
screen=pygame.display.set_mode((display_x, display_y))
lightgreen=(144, 238,144)





class BouncingBall():
	def __init__(self):
		self.circle_radius=20
		self.display_position_x=random.randint(self.circle_radius, display_x - self.circle_radius)
		self.display_position_y=random.randint(self.circle_radius, display_y - self.circle_radius)
		self.horizontal_speed=random.randint(1,10)
		self.vertical_speed=random.randint(1,10)
		
	def show(self):
		pygame.draw.circle(screen, (255, 255, 100), (self.display_position_x, self.display_position_y), self.circle_radius)
		
	def update(self):
		self.display_position_x+=self.horizontal_speed
		self.display_position_y+=self.vertical_speed
		if self.display_position_x+ self.circle_radius >= display_x or self.display_position_x- self.circle_radius <= 0:
			self.horizontal_speed *= -1
		if self.display_position_y+ self.circle_radius >= display_y or self.display_position_y- self.circle_radius <= 0:
			self.vertical_speed *=-1

total_ball_number=50
list_of_balls=[BouncingBall() for i in range(total_ball_number)]




game_running=True
while game_running:
	clock.tick(60)
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
	screen.fill(lightgreen)
	
	for i in range(total_ball_number):
		list_of_balls[i].show()
		list_of_balls[i].update()
	pygame.display.update()	
