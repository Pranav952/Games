import random
from turtle import Turtle, Screen
import random

screen = Screen()
turtle = Turtle()
colors = ["lime", "magenta", "darkgreen", "gold"]


def draw_shape(side):
    for i in range(side):
        angle = 360 / side
        color = random.choice(colors)
        turtle.color(color)
        turtle.forward(100)
        turtle.left(angle)


draw_shape(8)
screen.mainloop()
