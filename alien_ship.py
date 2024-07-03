import turtle
from turtle import Turtle

X = -395
Y = 280


class AlienShip(Turtle):

    def __init__(self):
        super().__init__()
        self.alien_shape = ((-50, 0), (-50, 20), (-40, 30), (-20, 30), (-30, 20),
                            (-30, 0), (-20, -10), (-40, -10))
        turtle.register_shape('alien_ship', self.alien_shape)
        self.shape('alien_ship')
        self.penup()
        self.x = X
        self.y = Y
        self.army_list = []

    def build_army(self, color, n):
        xn = self.x
        yn = self.y
        xn += n
        xnn = xn
        s = 0
        ir = 0
        while ir < 3:
            for i in range(3):
                alien = AlienShip()
                alien.color(color)
                s += 1
                alien.goto(xnn, yn)
                xnn += 80
                self.army_list.append(alien)
            yn -= 60
            xnn = xn
            ir += 1

    def y_move(self):
        for a in self.army_list:
            x_cor, y_cor = a.pos()
            a.goto(x_cor, y_cor - 25)
