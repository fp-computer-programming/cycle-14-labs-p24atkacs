#Author: Andrew Tkacs

#Computer Programming

#lab 14-3

import turtle

# Create a turtle window
window = turtle.Screen()
window.bgcolor("grey")
window.setup(width=500, height=500)
window.title("Lab 3")

# Create a turtle, changes my shape to the turtle and put color to blue.
t = turtle.Turtle()
t.shape("turtle")
t.color("blue")

# Move turtle to starting position
t.penup()
t.goto(0, 0)
t.pendown()

# Draw an equilateral triangle
for _ in range(3):
    t.forward(200)
    t.left(120)

# Keep the window open
window.mainloop()

#done
