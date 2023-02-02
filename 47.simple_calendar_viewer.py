#  Copyright 2022-2023 Mahid
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY
import time
import datetime
import calendar
import pygame,sys
from pygame.locals import*
pygame.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode((1200,650))

this_month=time.localtime()
month=this_month.tm_mon
year=this_month.tm_year
day=this_month.tm_yday
today=this_month.tm_mday

calendar.setfirstweekday(calendar.SUNDAY)


def return_calendar(year=year,month=month):
	cal=calendar.month(year,month)
	cal=cal.splitlines()
	cal.pop(0)
	dates=cal[0]
	dates=dates.split(' ')
	row2=cal[1]
	row2=row2.split(' ')
	cal.pop(0)
	r_txt=[]


	def calculate(row):
		row_txt=[]
		if len(row)%2==0:
			row=[row[i] for i in range(len(row)) if (i+1)%2==0]
		else:
			row=[row[i] for i in range(len(row)) if (i+1)%2!=0]
		x,y=0,len(row)
		x2,y2=x,y
		x3,y3=x,y
		row1=[item for item in row if item!='']
		n=7-len(row1)
		s=['' for i in range(n)]					
		if row[x2]=='' and row[-1]!='':
			while row[x2]=='':
				x2+=1
			new=s[:]+row[x2:]
			row_txt=new
		elif row[x3]!='' and row[-1]=='':
			while row[x3]!='':
				x3+=1
			new=row[:x3]+s[:]
			row_txt=new
		else:
			row_txt=row[:]
		r_txt.append(row_txt)
	calculate(row2)
	new=[]
	row1=cal[1]
	row1=row1.split(' ')
	row1=[item for item in row1 if item!='']
	n1=3
	if len(cal)==6:
		n1=4
	for i in range(n1):
		a=cal[i+2]
		a=a.split(' ')
		for j in range(1,len(a)+1):
			if a[j-1]!='':
				new.append(a[j-1])

	new=[item for item in new if item!='']
	x=r_txt[0]
	all_txt=dates+r_txt[0]+row1+new
	t=all_txt.index(str(today))
	return all_txt,t


all_rect=[]
def draw(x=7,y=7):
	y1=100
	for i in range(x):
		x1=100
		for i in range(y):	
			square=(x1,y1,70,70)
			all_rect.append(square)
			x1+=80
		y1+=80
draw()


txt_font=pygame.font.Font(pygame.font.get_default_font(),30)

def text_r(txt,c_rect,color="#4D4D4D"):

	rect_position=pygame.Rect(c_rect)
	
	pygame.draw.rect(screen,color,c_rect, border_radius=3)
	
	text_surface = txt_font.render(txt, 1,"#F0F8FF")
	txt_rect=text_surface.get_rect()
	txt_rect.center=rect_position.center
	screen.blit(text_surface,txt_rect)

def draw_txt():
	for i in range(len(all_txt)):
		if i<t:
			text_r(all_txt[i],all_rect[i])
		elif i==t:
			text_r(all_txt[i],all_rect[i],color='#000000')		
		else:
			text_r(all_txt[i],all_rect[i],color='#106b21')

while 1:
	clock.tick(10)
	all_txt,t=return_calendar()
	this_month=time.localtime()
	month=this_month.tm_mon
	year=this_month.tm_year
	day=this_month.tm_yday
	today=this_month.tm_mday
	for event in pygame.event.get():
		if event.type==QUIT:            
			pygame.quit()
			sys.exit()
			
	screen.fill((255,255,255))

	draw_txt()
	pygame.display.update()
