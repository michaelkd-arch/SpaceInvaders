import random
from turtle import Screen
import time
from projectile import Projectile
from tank import Tank
from scoreboard import Scoreboard
from alien_ship import AlienShip
from wall import Wall

order = False
order_start_time = time.time()
shooting_on = True
is_on = True
moves = 0
x_offset = 25
y_offset = 0

screen = Screen()
screen.bgcolor('black')
screen.setup(width=1000, height=800)
screen.title('Space Invaders')
screen.tracer(0)


tank = Tank()
sb = Scoreboard()
a_ship = AlienShip()

wall_x = -395
wall_y = -250

wall = Wall('black')

wall.build_wall('green', 0)
wall.build_wall('green', 350)
wall.build_wall('green', 700)


a_ship.build_army('yellow', 0)
a_ship.build_army('purple', 300)
a_ship.build_army('orange', 600)

screen.update()


def move_army():
    global moves, x_offset, y_offset, is_on, order, order_start_time, shooting_on

    if 3 > moves >= 0:
        for a in a_ship.army_list:
            x_cor, y_cor = a.pos()
            a.goto(x_cor - x_offset, y_cor)
        moves += 1
        time.sleep(0.5)
        order_end_time = time.time()
        if order_end_time - order_start_time > 2:
            if a_ship.army_list:
                r = Projectile('white')
                r.setheading(270)
                r.goto(random.choice(a_ship.army_list).pos())
                start_time = time.time()
                end_time = time.time()
                order = False
                while end_time - start_time < 1.6:
                    r.forward(2.9)
                    wall_collision(r)
                    end_time = time.time()
                    screen.update()
                    if r.distance(tank) < 37:
                        r.color('black')
                        sb.game_over()
                        is_on = False
                        shooting_on = False
                order = True
                r.color('black')
                order_start_time = time.time()
            else:
                sb.game_win()
                is_on = False
                shooting_on = False
    elif 6 > moves >= 3:
        for a in a_ship.army_list:
            x_cor, y_cor = a.pos()
            a.goto(x_cor + x_offset, y_cor)
        moves += 1
        time.sleep(0.5)
        order_end_time = time.time()
        if order_end_time - order_start_time > 2:
            r = Projectile('white')
            r.setheading(270)
            r.goto(random.choice(a_ship.army_list).pos())
            start_time = time.time()
            end_time = time.time()
            order = False
            while end_time - start_time < 1.6:
                r.forward(2.9)
                wall_collision(r)
                end_time = time.time()
                screen.update()
                if r.distance(tank) < 35:
                    r.color('black')
                    sb.game_over()
                    is_on = False
            order = True
            r.color('black')

            order_start_time = time.time()

    else:
        x_offset = - x_offset
        a_ship.y_move()
        moves = 0


def tank_shooting():
    global order
    r = Projectile('black')
    r.setheading(90)
    x_cor, y_cor = tank.pos()
    r.goto(x_cor + 25, y_cor + 60)
    r.color('white')
    start_time = time.time()
    end_time = time.time()
    while end_time - start_time < 1.6:
        order = False
        r.forward(6)
        wall_collision(r)
        end_time = time.time()
        screen.update()
        for a in a_ship.army_list:
            if a.distance(r) < 35:
                a.color('black')
                a.goto(-2000, -2000)
                r.color('black')
                r.goto(-2000, -2000)
                a_ship.army_list.remove(a)
                sb.score += 10
                sb.update_scoreboard()
    r.color('black')


def check_oder():
    global order
    if order and shooting_on:
        tank_shooting()
    else:
        return


def y_axis_ship():
    global is_on, shooting_on
    for a in a_ship.army_list:
        if a.pos()[1] <= -380:
            sb.game_over()
            is_on = False
            shooting_on = False


def wall_collision(pr):
    for w in wall.wall_list:
        if pr.distance(w) < 28:
            w.color('black')
            w.goto(-2000, -2000)
            wall.wall_list.remove(w)
            pr.color('black')
            pr.goto(-2000, -2000)


screen.onkeypress(tank.move_left, 'Left')
screen.onkeypress(tank.move_right, 'Right')
screen.onkeypress(check_oder, 'Up')

screen.listen()

while is_on:
    move_army()
    y_axis_ship()

    screen.update()


screen.exitonclick()
