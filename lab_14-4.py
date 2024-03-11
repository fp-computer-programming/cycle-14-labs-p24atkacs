#Author: Andrew Tkacs

#Computer Programming

#lab 14-4

import turtle

# Create a turtle window
window = turtle.Screen()
window.title("Lab 4")

# Create a turtle
t = turtle.Turtle()
t.speed(1)  # Set the speed of the turtle
t.color("red")  # Set the color of the turtle

# Create a stamp of the turtle at the origin
t.stamp()

# Move turtle to starting position
t.penup()
t.goto(100, 100)
t.pendown()

# Fill the square with another color
t.begin_fill()

# Draw a square
for _ in range(4):
    t.forward(100)
    t.right(90)

t.end_fill()

# Keep the window open
window.mainloop()

#done