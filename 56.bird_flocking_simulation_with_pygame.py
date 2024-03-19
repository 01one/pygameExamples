import pygame
import sys
import random
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()
display_x = 1200
display_y = 700
screen = pygame.display.set_mode((display_x, display_y))
lightgreen = (144, 238, 144)


class FlyingBird():
    def __init__(self):
        self.circle_radius = 2
        self.display_position_x = random.randint(self.circle_radius, display_x - self.circle_radius)
        self.display_position_y = random.randint(self.circle_radius, display_y - self.circle_radius)
        self.horizontal_speed = random.randint(-3, 3)
        self.vertical_speed = random.randint(-3, 3)

    def show(self):
        pygame.draw.circle(screen, (0, 0, 0), (self.display_position_x, self.display_position_y), self.circle_radius)

    def update(self, birds):
        center_of_mass_x = sum(b.display_position_x for b in birds) / len(birds)
        center_of_mass_y = sum(b.display_position_y for b in birds) / len(birds)

        self.horizontal_speed += (center_of_mass_x - self.display_position_x) * 0.001
        self.vertical_speed += (center_of_mass_y - self.display_position_y) * 0.001

        self.display_position_x += self.horizontal_speed
        self.display_position_y += self.vertical_speed

        if self.display_position_x + self.circle_radius >= display_x or self.display_position_x - self.circle_radius <= 0:
            self.horizontal_speed *= -1
        if self.display_position_y + self.circle_radius >= display_y or self.display_position_y - self.circle_radius <= 0:
            self.vertical_speed *= -1


total_bird_number = 1000
list_of_birds = [FlyingBird() for _ in range(total_bird_number)]

game_running = True
while game_running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(lightgreen)

    for bird in list_of_birds:
        bird.update(list_of_birds)
        bird.show()

    pygame.display.update()
