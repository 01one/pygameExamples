# Import the pygame library for game development
import pygame
# Import the sys module for system-specific parameters and functions
import sys
# Import specific constants from the pygame.locals module for easier access
from pygame.locals import *

# Initialize the pygame library
pygame.init()

# Create a clock object to control the frame rate
clock = pygame.time.Clock()
# Create a display surface with resizable dimensions (width: 1200, height: 600)
screen = pygame.display.set_mode((1200, 600), RESIZABLE)

# Define colors using RGB values and hexadecimal codes
colors = {
    "background": (240, 240, 240),
    "text": (50, 50, 50),
    "button_bg": (200, 200, 200),
    "button_border": (150, 150, 150),
    "button_hover": (220, 220, 220),
    "dropdown_bg": (220, 220, 220),
    "dropdown_border": (150, 150, 150),
    "dropdown_hover": (200, 200, 200),
    "dropdown_text": (50, 50, 50),
    "AliceBlue": "#F0F8FF",
    "Aqua": "#00FFFF",
    "FloralWhite": "#FFFAF0",
    "LightBlue": "#ADD8E6",
    "Ivory": "#FFFFF0",
    "Indigo": "#4B0082",
    "LightSkyBlue": "#87CEFA",
    "Maroon": "#800000",
    "Olive": "#808000",
    "MediumOrchid": "#BA55D3"
}

# Define constants for button and dropdown dimensions
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50
FONT_SIZE = 30
FONT_SMALL_SIZE = 20
DROPDOWN_POS_X = 50
DROPDOWN_POS_Y = 50
OPTION_HEIGHT = 40

# Initialize global variables for dropdown functionality
selected_option = 'Aqua'
show_options = False

# Define dropdown options
options = ["AliceBlue", "Aqua", "FloralWhite", "LightBlue", "Ivory", "Indigo", "LightSkyBlue", "Maroon", "Olive",
           "MediumOrchid"]

# Define function to draw the dropdown menu
def draw_dropdown():
    # Draw dropdown button
    button_color = colors["button_hover"] if show_options else colors["button_bg"]
    pygame.draw.rect(screen, button_color, (DROPDOWN_POS_X, DROPDOWN_POS_Y, BUTTON_WIDTH, BUTTON_HEIGHT))
    pygame.draw.rect(screen, colors["button_border"], (DROPDOWN_POS_X, DROPDOWN_POS_Y, BUTTON_WIDTH, BUTTON_HEIGHT), 2)

    # Render and position the text on the button
    font = pygame.font.Font(None, FONT_SIZE)
    text_surface = font.render(selected_option, True, colors["text"])
    text_rect = text_surface.get_rect(center=(DROPDOWN_POS_X + BUTTON_WIDTH / 2, DROPDOWN_POS_Y + BUTTON_HEIGHT / 2))
    screen.blit(text_surface, text_rect)

    # Draw dropdown options if the dropdown is expanded
    if show_options:
        # Draw each dropdown option
        for i, option in enumerate(options):
            option_y = DROPDOWN_POS_Y + BUTTON_HEIGHT + i * OPTION_HEIGHT
            option_rect = pygame.Rect(DROPDOWN_POS_X, option_y, BUTTON_WIDTH, OPTION_HEIGHT)
            option_color = colors["dropdown_hover"] if option_rect.collidepoint(pygame.mouse.get_pos()) else colors["dropdown_bg"]
            pygame.draw.rect(screen, option_color, option_rect)
            pygame.draw.rect(screen, colors["dropdown_border"], option_rect, 2)

            # Render and position the text for each option
            option_font = pygame.font.Font(None, FONT_SMALL_SIZE)
            option_surface = option_font.render(option, True, colors["dropdown_text"])
            option_rect = option_surface.get_rect(center=(DROPDOWN_POS_X + BUTTON_WIDTH / 2, option_y + OPTION_HEIGHT / 2))
            screen.blit(option_surface, option_rect)

# Main loop
game_running = True
while game_running:
    # Limit frame rate to 60 frames per second
    clock.tick(60)

    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            # Quit the pygame module and exit the system
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                # Check if an option is clicked when the dropdown is expanded
                if show_options:
                    for i, option in enumerate(options):
                        option_rect = pygame.Rect(DROPDOWN_POS_X, DROPDOWN_POS_Y + BUTTON_HEIGHT + i * OPTION_HEIGHT, BUTTON_WIDTH, OPTION_HEIGHT)
                        if option_rect.collidepoint(mouse_pos):
                            selected_option = option
                            show_options = False
                            break
                else:
                    # Toggle dropdown visibility if the button is clicked
                    if pygame.Rect(DROPDOWN_POS_X, DROPDOWN_POS_Y, BUTTON_WIDTH, BUTTON_HEIGHT).collidepoint(mouse_pos):
                        show_options = not show_options

    # Fill the screen with the selected background color
    screen.fill(colors[selected_option])
    # Draw the dropdown menu
    draw_dropdown()
    # Update the display
    pygame.display.update()
