import pygame,sys
from pygame.locals import*
pygame.init()

clock=pygame.time.Clock()
screen=pygame.display.set_mode((1200,600),RESIZABLE)

colors={"AliceBlue":"#F0F8FF","Aqua":"#00FFFF","FloralWhite":"#FFFAF0","LightBlue":"#ADD8E6","Ivory":"#FFFFF0","Indigo":"#4B0082","LightSkyBlue":"#87CEFA","Maroon":"#800000","Olive":"#808000","MediumOrchid":"#BA55D3"}
selected_option='Aqua'
show_options=False

class Option():
	def __init__(self,screen,btn_txt,c_rect,btn_color="#4D4D4D",corner=2,font_s=30,r=True,txt_in=True,txt='',selected=False):
		self.btn_txt=btn_txt
		self.x=c_rect[0]
		self.y=c_rect[1]
		self.x1=c_rect[2]
		self.y1=c_rect[3]
		self.btn_font=pygame.font.Font(pygame.font.get_default_font(),font_s)
		self.btn_color=btn_color
		self.color0="#AEC7CF"
		self.color1="#D81B1B"
		self.btn_position=pygame.Rect(self.x,self.y,self.x1,self.y1)
		self.button_txt=self.btn_font.render(self.btn_txt,True,self.color0)
		
		if self.btn_position.collidepoint(mouse_position):
			self.btn_color='#000000'
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button==1:
					if txt_in==True:		
						global selected_option
						selected_option=txt
	
					if selected==True:
						global show_options
						if show_options==False:
							show_options=True
		elif not self.btn_position.collidepoint(mouse_position):
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button==1:	
					show_options=False
						
		else:
			self.btn_color=self.btn_color
		if r==True:
				pygame.draw.rect(screen,self.btn_color, self.btn_position, border_radius=corner)
		txt_rect=self.button_txt.get_rect()
		txt_rect.center=self.btn_position.center
		screen.blit(self.button_txt,txt_rect)

color_list=["Background","AliceBlue","Aqua","FloralWhite","LightBlue","Ivory","Indigo","LightSkyBlue","Maroon","Olive","MediumOrchid"]
options=color_list
			
def option_view():
	if show_options==True:
		for i in range(len(options)):
			if i==0:
				Option(screen,options[i],(50,(10+40),200,50),selected=True,txt_in=False)
			else:
				Option(screen,options[i],(50,(50+i*40),200,50),txt=options[i],font_s=20)
	if show_options==False:
		Option(screen,options[0],(50,(10+40),200,50),txt=str(selected_option),txt_in=False,selected=True)


			
game_running=True
while game_running:
	color=colors[selected_option]
	clock.tick(60)
	
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
	mouse_position=pygame.mouse.get_pos()
	screen.fill(color)
	option_view()
	pygame.display.update()

