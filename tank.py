import turtle
from turtle import Turtle

STARTING_POSITION = (-20, -420)


class Tank(Turtle):

    def __init__(self):
        super().__init__()
        self.tank_shape = ((-50, 0), (-50, 20), (-60, 20), (-60, 30), (-50, 30),
                           (-50, 50), (-30, 50), (-30, 0))
        turtle.register_shape('tank', self.tank_shape)
        self.shape('tank')
        self.color('green')
        self.penup()
        self.goto(STARTING_POSITION)
        self.xn = STARTING_POSITION[0]

    def move_left(self):
        self.xn -= 20
        self.goto(self.xn, STARTING_POSITION[1])

    def move_right(self):
        self.xn += 20
        self.goto(self.xn, STARTING_POSITION[1])

