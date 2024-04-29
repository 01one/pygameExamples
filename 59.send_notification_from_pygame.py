import pygame
import sys
from pygame.locals import *
from plyer import notification

pygame.init()

clock = pygame.time.Clock()
user_display = pygame.display.Info()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

background = (255, 255, 255)
red = (255, 0, 0)
cornflower_blue = (128, 149, 255)
button_color = cornflower_blue
button_width, button_height = 250, 40
button_x = (width - button_width) // 2
button_y = (height - button_height) // 2

button_rect = pygame.Rect(button_x, button_y, button_width, button_height)


def button():
    pygame.draw.rect(screen, button_color, button_rect, border_radius=10)
    button_font = pygame.font.Font(pygame.font.get_default_font(), 20)
    button_text = button_font.render('Notification Button', True, (0, 0, 0))
    text_rect = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text, text_rect)


game_running = True
while game_running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect.collidepoint(event.pos):
                notification.notify(title='Notification', message='Notification From Pygame')
                print("notification sent")

        if event.type == pygame.MOUSEMOTION:
            if button_rect.collidepoint(event.pos):
                button_color = red
            else:
                button_color = cornflower_blue

    screen.fill(background)
    button()
    pygame.display.update()
