from turtle import Turtle


WALL_X = -395
WALL_Y = -250


class Wall(Turtle):

    def __init__(self, color):
        super().__init__()
        self.fillcolor(color)
        self.shape('square')
        self.shapesize(stretch_wid=0.5, stretch_len=2.5)
        self.x = WALL_X
        self.y = WALL_Y
        self.wall_list = []
        self.penup()

    def build_wall(self, color, n):
        xn = self.x
        yn = self.y
        xn += n
        for i in range(3):
            w = Wall(color)
            if i > 0:
                xn += 50
            w.goto(xn, yn)
            self.wall_list.append(w)
            