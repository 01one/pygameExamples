import pygame
import os

# Initialize Pygame
pygame.init()

# --- Screen setup ---
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
background_color = (255, 255, 255)  # White

# --- Load animation images ---
animation_folder = "sprite_images"  # We stored the animation frame images in this folder.
animation_images = []
for i in range(1, 11):  # Our images are "1.png" to "10.png"
    image_path = os.path.join(animation_folder, f"{i}.png")
    image = pygame.image.load(image_path)
    animation_images.append(image)

# --- Create the sprite ---
class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, animation_frames):
        super().__init__()
        self.frames = animation_frames
        self.current_frame = 0  # Start with the first frame
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height // 2)  # Center on screen.. You can apply responsive postion whatever the with or height is

    def update(self):
        # Cycle through animation frames
        self.current_frame += 1
        if self.current_frame >= len(self.frames):
            self.current_frame = 0
        self.image = self.frames[self.current_frame]

# Create an instance of our sprite
player_sprite = AnimatedSprite(animation_images)

# Group for easier drawing
all_sprites = pygame.sprite.Group()
all_sprites.add(player_sprite)

# --- Main game loop ---
running = True
clock = pygame.time.Clock()  # To control frame rate

while running:
    # --- Handle events ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Update the sprite's animation ---
    all_sprites.update()

    # --- Drawing ---
    screen.fill(background_color)
    all_sprites.draw(screen)
    pygame.display.flip()  # Update the display

    clock.tick(60)  # Limit to 60 frames per second

# Quit Pygame
pygame.quit()
