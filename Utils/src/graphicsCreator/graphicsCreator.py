# Program that generate visual graphics to draw any shape and design with colors
import tkinter as TK
import random
import turtle


colors = ['red', 'blue', 'yellow', 'green', 'white', 'grey', 'brown', 'purple']
t = turtle.Turtle()
t.speed(15) # Set the spiral rotation speed in secs
turtle.bgcolor("black")
length = 100
angle = 50
rad = 5

for i in range(length):
    color = random.choice(colors)
    t.pencolor(color)
    t.fillcolor(color)
    t.penup()
    t.forward(i+50)
    t.pendown()
    t.left(angle)
    t.begin_fill()
    t.circle(rad)
    t.end_fill()
turtle.exitonclick()
turtle.bgcolor("black")
