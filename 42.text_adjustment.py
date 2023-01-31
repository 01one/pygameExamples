import pygame,sys
from pygame.locals import*
pygame.init()
clock=pygame.time.Clock()
w=1000
h=600
screen=pygame.display.set_mode((w,h),RESIZABLE)

txt="""
The Æsop for Children
The Cock & the Fox
A Fox was caught in a trap one fine morning, because he had got too near the Farmer's hen house. No doubt he was hungry, but that was not an excuse for stealing. A Cock, rising early, discovered what had happened. He knew the Fox could not get at him, so he went a little closer to get a good look at his enemy.

The Fox saw a slender chance of escape.

"Dear friend," he said, "I was just on my way to visit a sick relative, when I stumbled into this string and got all tangled up. But please do not tell anybody about it. I dislike causing sorrow to anybody, and I am sure I can soon gnaw this string to pieces."

But the Cock was not to be so easily fooled. He soon roused the whole hen yard, and when the Farmer came running out, that was the end of Mr. Fox.

The wicked deserve no aid.
source: https://www.read.gov/aesop/145.html
"""


class TextView():
	def __init__(self,screen,text='',t_x=0,t_y=0,t_w=200,t_h=400,text_color="#666666"):
		self.screen=screen
		self.t_x=t_x
		self.t_y=t_y
		self.t_w=t_w
		self.t_h=t_h
		self.text_color=text_color 
		self.text=text
		self.text_font=pygame.font.Font('data/font/SortsMillGoudy-Italic.ttf', 22)
		self.text_lines=[]
		self.splitted_lines=self.text.splitlines()
		for splitted_line in self.splitted_lines:
			if self.text_font.size(splitted_line)[0] > self.t_w:
				words = splitted_line.split(' ')
				fitted_line=""
				for word in words:
					test_line = fitted_line + word + " "
					if self.text_font.size(test_line)[0] < self.t_w:
						fitted_line = test_line
					else:
						self.text_lines.append(fitted_line)
						fitted_line = word + " "
				self.text_lines.append(fitted_line)
			else:
				self.text_lines.append(splitted_line)
		text_row=self.t_y
		for line in self.text_lines:
			if line != "":
				text_surface = self.text_font.render(line, 1, self.text_color)
				self.screen.blit(text_surface, (self.t_x, self.t_y))
			self.t_y +=self.text_font.size(line)[1]

game_running=True
while game_running:
	clock.tick(60)
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
		if event.type==pygame.VIDEORESIZE:
			w,h=event.size
	screen.fill('#F0FFFF')
	TextView(screen,text=txt,t_x=20,t_y=10,t_w=w-50,t_h=h)
	pygame.display.update()
