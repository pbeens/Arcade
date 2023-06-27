import random
import arcade
import time
import threading

# Step 1: Initialize a "numbers" list with each number from 1 to 10 in a randomized order.
numbers = random.sample(range(1, 11), 10)

# Step 2: Using the Arcade library, draw a bar chart representing the 10 numbers in that list.
WIDTH = 800
HEIGHT = 600
BAR_WIDTH = 50
BAR_MARGIN = 10
BAR_COLOR = arcade.color.BLUE
BAR_HEIGHT_SCALE = 40  # Adjust the scaling factor to double the height of the bars

def draw_barchart(delta_time):
    """
    Function to draw the bar chart using Arcade library.
    """
    arcade.start_render()

    x = WIDTH // 2 - (BAR_WIDTH + BAR_MARGIN) * len(numbers) // 2
    for i, number in enumerate(numbers):
        bar_height = number * BAR_HEIGHT_SCALE  # Scale the height of the bar
        arcade.draw_rectangle_filled(x, bar_height // 2, BAR_WIDTH, bar_height, BAR_COLOR)
        x += BAR_WIDTH + BAR_MARGIN

def bubble_sort():
    """
    Function to perform bubble sort on the numbers list.
    """
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                time.sleep(0.5)  # Introduce a delay of 0.5 seconds between swaps
                arcade.schedule(draw_barchart, 0)

def main():
    """
    Main function to initialize the window, schedule rendering, and start the sorting process.
    """
    arcade.open_window(WIDTH, HEIGHT, "Bubble Sort")  # Set the window title to "Bubble Sort"
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(draw_barchart, 1 / 60)  # Redraw the chart at 60 FPS
    
    sorting_thread = threading.Thread(target=bubble_sort)  # Create a separate thread for sorting
    sorting_thread.start()  # Start the sorting process in the background thread

    arcade.run()

if __name__ == "__main__":
    main()
