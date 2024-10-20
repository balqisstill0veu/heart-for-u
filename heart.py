import math
from turtle import *
from PIL import Image

# Define the heart shape functions
def hearta(k):
    return 15 * math.sin(k) ** 3

def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

# Set up the Turtle
speed(0)  # Set the speed of the drawing
bgcolor("black")  # Set the background color
color("red")  # Set the heart color
penup()  # Lift the pen to move to the starting point
goto(0, 0)  # Move the turtle to the center of the screen
pendown()  # Put the pen down to start drawing

# Draw the heart shape
for i in range(3000):  # Loop to plot the heart shape
    x = hearta(i / 100) * 20
    y = heartb(i / 100) * 20
    goto(x, y)

# Keep the window open for a few seconds to display the heart
import time
time.sleep(5)  # Keep the window open for 5 seconds

# Save the drawing as an image using canvas and PIL
canvas = getcanvas()
canvas.postscript(file="heart.eps")  # Save as an .eps file

# Convert .eps to .png using Pillow
img = Image.open("heart.eps")
img.save("heart_image.png")  # Save as a PNG image

done()  # Close the Turtle window after the drawing is finished
