import sys
import pygame
import matplotlib
from pygame.locals import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

# Initialize Pygame
pygame.init()

# Set up the display window
clock = pygame.time.Clock()  # Used to control the speed of the game loop
display_screen = pygame.display.set_mode((1200, 600))  # Create a window 1200 pixels wide, 600 pixels tall
background_color = (144, 238, 144)  # A light green color

# Create the Matplotlib plot 
figure, axis = plt.subplots()  # Create a figure (the container) and an axis (for plotting)
axis.plot([1, 2, 3, 4, 5, 6, 7], [10, 20, 25, 30, 25, 45, 50])  # Plot sample data 
plot_canvas = FigureCanvas(figure)  # Create a canvas to render the Matplotlib plot 

# Main game loop
running = True
while running:
    clock.tick(10)  # Limit the loop to run 10 times per second

    # Handle events (like keyboard presses, mouse clicks)
    for event in pygame.event.get():
        if event.type == QUIT:  # Check if the user clicked the close button
            pygame.quit()
            sys.exit()

    # Clear the screen with the background color
    display_screen.fill(background_color)

    # Draw the Matplotlib plot onto the Pygame screen
    plot_canvas.draw()  # Update the Matplotlib plot if needed
    renderer = plot_canvas.get_renderer()  
    matplotlib_plot_rgba_image_data = renderer.tostring_rgb()  # Get raw image data of the plot
    plot_canvas_width, plot_canvas_height = plot_canvas.get_width_height() 

    # Convert the Matplotlib image data into a Pygame surface
    plot_surface = pygame.image.fromstring(matplotlib_plot_rgba_image_data, 
                                           (plot_canvas_width, plot_canvas_height), 
                                           "RGB")

    # Display the plot on the Pygame screen
    display_screen.blit(plot_surface, (300, 50))  # Place the plot at position (300, 50)

    # Update the display to show changes
    pygame.display.update()
