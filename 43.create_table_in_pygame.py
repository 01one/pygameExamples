import pygame,sys
from pygame.locals import*
pygame.init()
screen=pygame.display.set_mode((1000,650),RESIZABLE)
font=pygame.font.Font('data/font/Genos-Bold.ttf', 20)

class Label():
	def __init__(self,label_txt,x,y,x1,y1):
		self.label_txt=label_txt
		self.x=x
		self.y=y
		self.x1=x1
		self.y1=y1
		self.label_font=font
		self.label_color="#4D4D4D"
		self.color0="#AEC7CF"
		self.color1="#D81B1B"
		self.label_position=pygame.Rect(self.x,self.y,self.x1,self.y1)
		self.label_txt=self.label_font.render(self.label_txt,True,self.color0)
		self.mouse_position=pygame.mouse.get_pos()
		pygame.draw.rect(screen,self.label_color, self.label_position, border_radius=2)
		txt_rect=self.label_txt.get_rect()
		txt_rect.center=self.label_position.center
		screen.blit(self.label_txt,txt_rect)

programming_language=["c","cpp","rust","python"]
filename_extension=[".c",".cpp", ".rs",".py"]


game_running=True
while game_running:
	for event in pygame.event.get():
		if event.type==QUIT:            
			pygame.quit()
			sys.exit()
	screen.fill((255,255,255))
	pygame.draw.rect(screen,"#601B1B",(70,10,300,200))
	for i in range(1,5):
		for j in range(1,3):
			if i==1 and j==1:
				Label("Language",j*75,i*30,85,20)
			if i==1 and j==2:
				Label("Extension",j*85,i*30,85,20)
				 
			if j==1:
				Label(programming_language[i-1],j*90,(i+1)*30,60,20)
				Label(filename_extension[i-1],(j+1)*90,(i+1)*30,60,20)
	
	pygame.display.update()
