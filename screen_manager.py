from turtle import Turtle
import constants

class ScreenManager():
    def __init__(self):
        self.drawer = Turtle()
        self.line_list = []
        self.drawer.hideturtle()
        self.x_coor = -550
        self.speed = constants.STARTING_SPEED
        self.draw_grass()
        self.draw_grass()
        self.create_lines()

    def draw_grass(self):
        self.drawer.penup()
        self.drawer.width(100)
        self.drawer.goto(self.x_coor, -350)
        self.drawer.color('chartreuse')
        self.drawer.setheading(90)
        self.drawer.pendown()
        self.drawer.forward(700)
        self.x_coor = 550

    def create_lines(self):
        my_horizontal = self.x_coor - 50
        for n in range(4):
            my_horizontal -= 200
            my_vertical = 350+150
            for m in range(6):
                my_vertical -= 150
                turtle = Turtle()
                turtle.penup()
                turtle.color('white')
                turtle.shape("square")
                turtle.setheading(270)
                turtle.turtlesize(0.1, 5, 1)
                turtle.goto(my_horizontal, my_vertical)
                self.line_list.append(turtle)

    def move_road(self):
        for line in self.line_list:
            for n in range(self.speed):
                line.forward(1)
                if line.ycor() < -400:
                    line.sety(400)

    def speed_up(self):
        if self.speed < constants.MAX_SPEED:
            self.speed += 1

    def game_over(self):
        self.drawer.penup()
        self.drawer.goto(0,0)
        self.drawer.color("red")
        self.drawer.write("GAME OVER", align='center', font=('Courier', 40, 'normal'))
