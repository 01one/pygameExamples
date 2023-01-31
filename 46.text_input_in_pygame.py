import pygame,sys,time
from pygame.locals import*
pygame.init()
clock=pygame.time.Clock()

w=1000
h=600

screen=pygame.display.set_mode((w,h),RESIZABLE)
then=time.time()
txt=""
pulse='|'
font=pygame.font.Font(pygame.font.get_default_font(),22)


class TextView():
	def __init__(self,screen,text='',t_x=0,t_y=0,t_w=200,t_h=400,text_color="#666666",pulse=''):
		self.screen=screen
		self.t_x=t_x
		self.t_y=t_y
		self.t_w=t_w
		self.t_h=t_h
		self.text_color=text_color 
		self.text=text+pulse
		self.text_font=font
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
				if all_select==True:
					first_line=(self.text_font.render(self.text_lines[0], 1, self.text_color)).get_rect()
					txt_rect=text_surface.get_rect()
					txt_rect=(self.t_x,self.t_y,txt_rect[2],txt_rect[3])
					pygame.draw.rect(screen,"#ccffcc",txt_rect)
				self.screen.blit(text_surface, (self.t_x, self.t_y))
			self.t_y +=self.text_font.size(line)[1]

			
all_select=False
game_running=True
Next_line=False
while game_running:
	clock.tick(60)
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
		if event.type==pygame.VIDEORESIZE:
			w,h=event.size
		if event.type==pygame.TEXTINPUT:
			txt+=event.text
			all_select=False
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_BACKSPACE:
				pygame.key.set_repeat(200,5)
				if len(txt)==0:
					pass
				else:
					txt=txt[:-1]
				if all_select==True:
					txt=''
					all_select=False
					
					
			if event.key==pygame.K_a:
				if event.mod == pygame.KMOD_NONE:
					continue
				else:
					if event.mod & pygame.KMOD_LCTRL:
						all_select=True
						
			if event.key==pygame.K_RETURN:
				Next_line=True
			
				
	now=time.time()
	d=now-then
	if d>=1 and d<=2:
		then=now
		pulse=''
	else:
		pulse='|'
	if Next_line==True:
		txt=txt+'\n'
		Next_line=False
	screen.fill('#F0FFFF')
	TextView(screen,text=txt,t_x=20,t_y=10,t_w=w-50,t_h=h,pulse=pulse)
	pygame.display.update()
