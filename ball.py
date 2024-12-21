from turtle import Turtle
from random import randint
BALLPOSITION = (-355, 0)
BALLRANGE = (-60, 60)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        # self.shapesize(stretch_wid =0.5,stretch_len=0.5, outline= 0)
        self.speed(10)
        self.penup()
        self.goto(BALLPOSITION)
        self.setheading(randint(a = -70, b= 70))
        ball_x = self.xcor()
        ball_y = self.ycor()


    def move(self):
        self.forward(5)

    def bounce(self):
        self.setheading(self.heading() * -1)

    def bounce_y(self):
        self.setheading(self.heading() + 180)
        self.setheading(self.heading() * -1)
