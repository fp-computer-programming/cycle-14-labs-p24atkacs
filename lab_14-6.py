#Author: Andrew Tkacs

#computer programming

#lab 14-6

import turtle
import tkinter as tk  #I used tkinter for entry widget for color and size.

# Create a turtle window
window = turtle.Screen()
window.title("Lab 6")

# Create a turtle
t = turtle.Turtle()

# Prompt the user for a color
color = tk.simpledialog.askstring("Color", "Enter a color:")

# Prompt the user for a size
size = tk.simpledialog.askinteger("Size", "Enter a size (1-5):", minvalue=1, maxvalue=5)

# Change the turtle to the color and size input by the user

t.color(color)
t.shapesize(size)

# Function to draw a square at the clicked position

def draw_square(x, y):
    t.penup()
    t.goto(x - 50, y + 50)
    t.setheading(0)
    t.pendown()
    t.begin_fill()
    for _ in range(4):
        t.forward(100)
        t.right(90)
    t.end_fill()

# Bind the draw_square function to the onclick event
turtle.onscreenclick(draw_square)

# Keep the window open

window.mainloop()

#done 


