import pygame
import sys
import math
import random
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

class Person:
    def __init__(self, name, position, radius, color):
        self.name = name
        self.position = position
        self.radius = radius
        self.color = color
        self.friends = []

    def show(self):
        pygame.draw.circle(screen, self.color, (int(self.position[0]), int(self.position[1])), self.radius)
        font = pygame.font.Font(None, 24)
        text = font.render(self.name, True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.position[0], self.position[1] + self.radius + 15))
        screen.blit(text, text_rect)

    def make_friends(self, other_person):
        self.friends.append(other_person)
        other_person.friends.append(self)

    def connect(self, other_person):
        self.make_friends(other_person)

    def draw_connections(self):
        for friend in self.friends:
            pygame.draw.line(screen, self.color, self.position, friend.position, 1)

def get_hovered_person(pos, persons):
    for person in persons:
        if math.sqrt((pos[0] - person.position[0])**2 + (pos[1] - person.position[1])**2) <= person.radius:
            return person
    return None

def find_second_degree_connections(person):
    second_degree = set()
    for friend in person.friends:
        second_degree.add(friend)
        for friend_of_friend in friend.friends:
            second_degree.add(friend_of_friend)
    return second_degree

def find_third_degree_connections(person):
    third_degree = set()
    for friend in person.friends:
        third_degree.add(friend)
        for friend_of_friend in friend.friends:
            third_degree.add(friend_of_friend)
            for friend_of_friend_of_friend in friend_of_friend.friends:
                third_degree.add(friend_of_friend_of_friend)
    return third_degree

def visualize_all_connections():
    for person in list_of_persons:
        second_degree = find_second_degree_connections(person)
        third_degree = find_third_degree_connections(person)
        for p in second_degree:
            pygame.draw.line(screen, (255, 255, 255), person.position, p.position, 1)
        for p in third_degree:
            pygame.draw.line(screen, (255, 255, 255), person.position, p.position, 1)

total_persons = 50
list_of_persons = []

names = [
    "Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Henry", "Ivy", "Jack",
    "Kate", "Liam", "Mia", "Noah", "Olivia", "Peter", "Quinn", "Rachel", "Sam", "Taylor",
    "Uma", "Victor", "Wendy", "Xander", "Yara", "Zane",
    "Abigail", "Benjamin", "Chloe", "Daniel", "Ella", "Finn", "Georgia", "Hannah", "Isaac",
    "Jessica", "Kevin", "Lily", "Mason", "Natalie", "Oscar", "Penelope", "Quentin", "Rebecca",
    "Samantha", "Thomas", "Ursula", "Violet", "William", "Xavier", "Yasmine", "Zoe"
]


for i in range(total_persons):
    radius = random.randint(20, 30)
    position = [random.randint(radius, display_x - radius), random.randint(radius, display_y - radius)]
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    list_of_persons.append(Person(names[i], position, radius, color))

# Connect some random friends up to the first degree
for i, person in enumerate(list_of_persons):
    for j in range(i+1, len(list_of_persons)):
        if random.random() < 0.08:  # Randomly connect each person with 20% chance
            person.connect(list_of_persons[j])

game_running = True

while game_running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(lightgreen)
    
    hovered_person = get_hovered_person(pygame.mouse.get_pos(), list_of_persons)
    if hovered_person:
        second_degree = find_second_degree_connections(hovered_person)
        third_degree = find_third_degree_connections(hovered_person)
        for person in second_degree:
            pygame.draw.line(screen, (255, 255, 255), hovered_person.position, person.position, 1)
        for person in third_degree:
            pygame.draw.line(screen, (255, 255, 255), hovered_person.position, person.position, 1)

    for person in list_of_persons:
        person.show()

    draw_button(20, 20, 150, 50, "Visualize All", visualize_all_connections)

    pygame.display.update()
    clock.tick(60)
