from turtle import Turtle


class Projectile(Turtle):

    def __init__(self, color):
        super().__init__()
        self.shape('circle')
        self.color(color)
        self.shapesize(stretch_wid=0.3)
        self.penup()
        self.speed(5)
