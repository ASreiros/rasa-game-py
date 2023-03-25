from turtle import Turtle
from random import randint
import constants


class Traffic:
    def __init__(self):
        self.traffic_list = []
        self.garage_list = []
        self.speed = constants.STARTING_SPEED

    def add_car(self):
        if len(self.garage_list) == 0:
            traffic_car = Turtle()
        else:
            traffic_car = self.garage_list.pop(0)
        traffic_car.hideturtle()
        traffic_car.penup()
        traffic_car.setheading(90)
        flag = False
        while not flag:
            flag = True
            line = randint(-2, 2)
            x = 200*line
            traffic_car.goto(x=x, y=400)
            for other_car in self.traffic_list:
                if x+30 > int(other_car.xcor()) > x-30:
                    flag = False
        nr = randint(1, 7)
        traffic_car.shape(f'./img/car{nr}.gif')
        traffic_car.showturtle()
        self.traffic_list.append(traffic_car)

    def speed_up(self):
        if self.speed < constants.MAX_SPEED:
            self.speed += 1

    def move_traffic(self):
        for n in range(len(self.traffic_list)):
            car = self.traffic_list[n]
            for _ in range(self.speed):
                car.backward(1)
            if car.pos()[1] < -500:
                car.hideturtle()
                self.garage_list.append(car)
        for car in self.garage_list:
            if car in self.traffic_list:
                self.traffic_list.remove(car)

    def collision(self, turtle):
        collision_flag = False
        car_line = turtle.xcor()
        for tr_car in self.traffic_list:
            if tr_car.distance(turtle) < 180 and car_line+50 > tr_car.xcor() > car_line - 50:
                collision_flag = True
        return collision_flag

