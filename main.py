import random
import turtle

import colorgram
from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
turtle.colormode(255)

colors_p = colorgram.extract('image.jpeg', 30)
rgp_color = []
for color in colors_p:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgp_color.append((r, g, b))

print(rgp_color)


def hirst_painting():
    timmy.penup()
    timmy.hideturtle()
    timmy.speed('fastest')
    for i in range(1, 11):
        for j in range(1, 11):
            timmy.dot(20, random.choice(rgp_color))
            timmy.forward(50)
        timmy.home()
        timmy.teleport(y=timmy.ycor() + 50 * i)


hirst_painting()

screen.exitonclick()
