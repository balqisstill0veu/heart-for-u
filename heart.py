import math
from turtle import *
from PIL import Image

# Define the heart shape
def hearta(k):
    return 15 * math.sin(k) ** 3

def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

# Set up the Turtle
speed(0)  # Set the speed of the drawing
bgcolor("black")  # Set the background color
color("red")  # Set the color of the heart
penup()  # Lift the pen to start from the center
goto(0, 0)  # Move the turtle to the center of the screen
pendown()  # Put the pen down to start drawing

# Draw the heart shape
for i in range(3000):  # Loop to plot the heart shape
    x = hearta(i / 100) * 20
    y = heartb(i / 100) * 20
    goto(x, y)

# Save the drawing as an image using canvas and PIL
canvas = getcanvas()
canvas.postscript(file="heart.eps")  # Save as a .eps file (Encapsulated PostScript)

# Convert .eps to .png using Pillow
img = Image.open("heart.eps")
img.save("heart_image.png")  # Save as a PNG image

done()
