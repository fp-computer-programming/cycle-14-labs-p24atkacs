
#Author: Andrew Tkacs

#computer programming

#lab 14-1


import turtle

#creating my turtle screen

screen= turtle.Screen()
screen.setup(width=1000, height=1000)
screen.title("lab 1")

#the turtle

bob= turtle.Turtle()

#rectangle - moving point to top left

bob.penup()
bob.goto(0,0)
bob.pendown()

bob.forward(250)
bob.right(90)
bob.forward(100)
bob.right(90)
bob.forward(250)
bob.right(90)
bob.forward(100)

turtle.done()

#done

