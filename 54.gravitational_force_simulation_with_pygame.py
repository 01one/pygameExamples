import pygame
import sys
import random
import math
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()
display_x = 1600
display_y = 900
screen = pygame.display.set_mode((display_x, display_y))
lightgreen = (144, 238, 144)

def draw_button(x, y, width, height, text, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        pygame.draw.rect(screen, (0, 255, 0), (x, y, width, height))
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(screen, (0, 200, 0), (x, y, width, height))

    small_text = pygame.font.Font(None, 20)
    text_surf, text_rect = text_objects(text, small_text)
    text_rect.center = ((x + (width / 2)), (y + (height / 2)))
    screen.blit(text_surf, text_rect)


def text_objects(text, font):
    text_surface = font.render(text, True, (0, 0, 0))
    return text_surface, text_surface.get_rect()

class SpaceObject:
    def __init__(self, position, radius, mass, color):
        self.position = position
        self.radius = radius
        self.mass = mass
        self.color = color
        self.velocity = [0, 0]
        self.acceleration = [0, 0]

    def show(self):
        pygame.draw.circle(screen, self.color, (int(self.position[0]), int(self.position[1])), self.radius)

    def update(self):
        self.velocity[0] += self.acceleration[0]
        self.velocity[1] += self.acceleration[1]
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        
        if boundary_enabled:
            self.position[0] = self.position[0] % display_x
            self.position[1] = self.position[1] % display_y

    def apply_force(self, force):
        self.acceleration[0] += force[0] / self.mass
        self.acceleration[1] += force[1] / self.mass

def collide(obj1, obj2):
    dx = obj2.position[0] - obj1.position[0]
    dy = obj2.position[1] - obj1.position[1]
    distance = math.sqrt(dx ** 2 + dy ** 2)

    if distance < obj1.radius + obj2.radius:
        total_mass = obj1.mass + obj2.mass
        obj1.velocity = [((obj1.mass - obj2.mass) * obj1.velocity[0] + 2 * obj2.mass * obj2.velocity[0]) / total_mass,
                         ((obj1.mass - obj2.mass) * obj1.velocity[1] + 2 * obj2.mass * obj2.velocity[1]) / total_mass]
        obj1.mass += obj2.mass
        obj1.radius = int(obj1.mass ** (1/3))
        return True
    return False


total_object_number = 200
list_of_objects = []

for _ in range(total_object_number):
    radius = random.randint(2, 5)
    mass = radius ** 3
    position = [random.randint(radius, display_x - radius), random.randint(radius, display_y - radius)]
    velocity = [random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5)]
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    list_of_objects.append(SpaceObject(position, radius, mass, color))

num_suns = 3
for _ in range(num_suns):
    sun_mass = random.randint(5000, 20000)
    sun_radius = int(sun_mass ** (1/3))
    sun_position = [random.randint(sun_radius, display_x - sun_radius), random.randint(sun_radius, display_y - sun_radius)]
    sun_color = (255, 255, 0)
    list_of_objects.append(SpaceObject(sun_position, sun_radius, sun_mass, sun_color))

boundary_enabled = False
def toggle_boundary():
    global boundary_enabled
    boundary_enabled = not boundary_enabled

game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(lightgreen)
    if boundary_enabled:
        draw_button(10, 10, 200, 50, 'Remove Boundary', toggle_boundary)
    else:
        draw_button(10, 10, 200, 50, 'Add Boundary', toggle_boundary)
    for obj in list_of_objects:
        obj.acceleration = [0, 0]  
        for heavy_object in list_of_objects:
            if obj != heavy_object:
                dx = heavy_object.position[0] - obj.position[0]
                dy = heavy_object.position[1] - obj.position[1]
                distance_squared = dx ** 2 + dy ** 2
                force_magnitude = 0.5 * (heavy_object.mass / distance_squared)
                force_direction = [dx / math.sqrt(distance_squared), dy / math.sqrt(distance_squared)]
                obj.apply_force([force_magnitude * force_direction[0], force_magnitude * force_direction[1]])

        obj.update()
        obj.show()


    for obj in list_of_objects:
        for heavy_object in list_of_objects:
            if obj != heavy_object:
                if collide(heavy_object, obj):
                    list_of_objects.remove(obj)
                    break  



    pygame.display.update()
    clock.tick(60)
