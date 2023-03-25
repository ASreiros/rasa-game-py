import turtle
from turtle import Turtle, Screen
import time
from screen_manager import ScreenManager
from car import Car
from traffic import Traffic

screen = Screen()
screen.setup(width=1200, height=700)
screen.bgcolor("dark gray")
screen.title("Race game")
screen.tracer(0)
turtle.register_shape('./img/main_car.gif')
turtle.register_shape('./img/car1.gif')
turtle.register_shape('./img/car2.gif')
turtle.register_shape('./img/car3.gif')
turtle.register_shape('./img/car4.gif')
turtle.register_shape('./img/car5.gif')
turtle.register_shape('./img/car6.gif')
turtle.register_shape('./img/car7.gif')
manager = ScreenManager()
player = Car()
traffic = Traffic()
screen.listen()
screen.onkey(player.press_left, "Left")
screen.onkey(player.press_right, "Right")

traffic.add_car()
speed_counter = 30
traffic_counter = 20
game_is_on = True
countdown = 3
while game_is_on:
    screen.update()
    manager.move_road()
    traffic.move_traffic()
    speed_counter -= 1
    traffic_counter -= 1
    if speed_counter == 0:
        speed_counter = 30
        manager.speed_up()
        traffic.speed_up()
    if traffic_counter < 1 and len(traffic.traffic_list) < 3:
        traffic.add_car()
    if traffic.collision(player):
        countdown -= 1
        if countdown <= 0:
            manager.game_over()
            game_is_on = False
    time.sleep(0.1)


screen.exitonclick()