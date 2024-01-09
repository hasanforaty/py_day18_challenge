import random
import turtle
from turtle import Turtle, Screen

color_list = ['red', 'orange', 'yellow', 'green', 'blue',
              'purple', 'pink', 'brown', 'gray', 'gold', 'cyan', 'Gainsboro', 'gray',
              'dimgray', 'LightSlateGray', 'AliceBlue', 'LimeGreen', 'DarkKhaki', 'Khaki']

timmy = Turtle()
screen = Screen()

timmy.color("blue")


def turtle_square(length: int):
    """challenge 1 : draw a square"""
    for i in range(0, 4):
        timmy.forward(length)
        timmy.left(90)


def draw_dash_line(length: int, space=10, line_length=10):
    """challenge 2 : draw a dash line"""
    total_distance = 0
    while total_distance < length:
        timmy.pendown()
        timmy.forward(line_length)
        timmy.penup()
        timmy.forward(space)
        total_distance += space + line_length


def draw_shapes(length: int):
    """challenge 3 :draw shape 3 to 10 side with random color for each shape"""
    total_degree = 360
    for i in range(3, 11):
        angle = total_degree / i
        timmy.color(random.choice(color_list))
        for j in range(0, i):
            timmy.forward(length)
            timmy.left(angle)


# turtle_square(100)
# draw_dash_line(length=200)
draw_shapes(100)

screen.exitonclick()
