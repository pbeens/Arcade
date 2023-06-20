# Import arcade library
import arcade
# Import random library
import random

# Define constants for the screen size
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
SCREEN_TITLE = "Bird Example"

# Define variables for the bird parameters
bird_size = 20
bird_color = arcade.color.BLACK
bird_border_width = 5


# Define a function to draw a bird using two arcs
def draw_bird(x, y, size, color, border_width):
    # Draw the left arc with start angle of 0 and end angle of 90
    arcade.draw_arc_outline(x, y, size, size,
                            color, 0, 90,
                            border_width)
    # Draw the right arc with start angle of 90 and end angle of 180
    # Adjust the x position by the size to make the arcs touch at the bottom
    arcade.draw_arc_outline(x + size, y, size, size,
                            color, 90, 180,
                            border_width)


# Open the window
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
# Set the background color to white
arcade.set_background_color(arcade.color.WHITE)
# Start the render process
arcade.start_render()
# Draw 10 birds using the draw_bird function with random x and y positions
for i in range(10):
    # Generate random x and y positions within the screen boundaries
    bird_x = random.randint(0, SCREEN_WIDTH - bird_size * 2)
    bird_y = random.randint(0, SCREEN_HEIGHT - bird_size)
    # Draw a bird using the function and the variables
    draw_bird(bird_x, bird_y, bird_size, bird_color, bird_border_width)
# Finish the render
arcade.finish_render()
# Run the program
arcade.run()
