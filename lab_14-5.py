#Author: Andrew Tkacs

#Computer Programming

#Lab 14-5

import turtle

def move_forward():
    t.forward(10)

def move_backward():
    t.backward(10)

def turn_left():
    t.left(90)

def turn_right():
    t.right(90)

# Create a turtle window
window = turtle.Screen()
window.title("Lab 5")

# Create a turtle
t = turtle.Turtle()

# Set key bindings
window.listen()
window.onkey(move_forward, "Up")
window.onkey(move_backward, "Down")
window.onkey(turn_left, "Left")
window.onkey(turn_right, "Right")

# Keep the window open
window.mainloop()

#done