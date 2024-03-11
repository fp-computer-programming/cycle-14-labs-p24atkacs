
#author: Andrew Tkacs

#computer programming

#lab 14-2

import turtle

# Create a turtle window
window = turtle.Screen()
window.setup(width=500, height=500)
window.title("Lab 2")

# Create a turtle
t = turtle.Turtle()

# Move turtle to starting position
t.penup()
t.goto(0, -50)
t.pendown()

# Draw an equilateral triangle
for _ in range(3):
    t.forward(100)
    t.left(120)

# Keep the window open
window.mainloop()

#done
