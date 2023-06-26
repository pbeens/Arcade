import arcade
import random

# Define the number of circles in each row and column
rows = 20
cols = 30

# Define the window size
window_width = 800
window_height = 600

# Define the minimum and maximum circle size
min_size = 3
max_size = 10

# Define the horizontal and vertical spacing between circles
h_spacing = (window_width - 100) // cols
v_spacing = (window_height - 100) // rows


def draw_circle(x, y):
    """
    Draws a filled circle with a randomly generated color and size at a given position.

    Args:
        x (int): The x-coordinate of the circle's center.
        y (int): The y-coordinate of the circle's center.

    Returns:
        None
    """
    # Pick a random color that is not too dark
    r = random.randint(100, 255)
    g = random.randint(100, 255)
    b = random.randint(100, 255)
    color = (r, g, b)

    # Pick a random size
    size = random.randint(min_size, max_size)

    # Draw a filled circle
    arcade.draw_circle_filled(x, y, size, color)


# Create a window with a black background
window = arcade.open_window(
    window_width, window_height, "Grid of Circles (Arcade Version)")
arcade.set_background_color(arcade.color.BLACK)

# Start the render process
arcade.start_render()

# Draw a grid of circles
for i in range(rows):
    for j in range(cols):
        # Calculate the x and y coordinates of the circle
        x = h_spacing / 2 + j * h_spacing + 50
        y = window_height - v_spacing / 2 - i * v_spacing - 50

        # Draw a circle
        draw_circle(x, y)

# Finish the render process
arcade.finish_render()

# Run the window until closed by the user
arcade.run()
