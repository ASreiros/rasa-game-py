from turtle import Turtle

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.setx = 0
        self.hideturtle()
        self.penup()
        self.sety(-200)
        self.setheading(0)
        self.showturtle()
        self.shape('./img/main_car.gif')

    def press_left(self):
        coordinates = self.pos()
        if coordinates[0] > -400:
            self.goto(coordinates[0] - 200, coordinates[1])

    def press_right(self):
        coordinates = self.pos()
        if coordinates[0] < 400:
            self.goto(coordinates[0] + 200, coordinates[1])
