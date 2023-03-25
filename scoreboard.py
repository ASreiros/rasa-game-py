from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(400, 300)
        self.score = -1

    def score_up(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", font=("Courier", 20, 'normal'))
