import turtle
from turtle import Turtle
import random

TOP = 240
BOTTOM = -240
SPREAD = 20
LANES = [i for i in range(BOTTOM, TOP, SPREAD)]

turtle.colormode(255)


def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def choose_random_lane():
    return random.choice(LANES)


class Car(Turtle):
    def __init__(self):
        super().__init__("square")
        self.penup()
        self.color(get_random_color())
        self.shapesize(1, 3)
        self.setpos(280, choose_random_lane())

    def move(self):
        new_x = self.xcor() - 10
        self.setpos(new_x, self.ycor())



