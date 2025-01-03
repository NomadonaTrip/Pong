from turtle import Turtle
PLAYERPOSITION= (380,0)
COMPUTERPOSITION = (-380, 0)


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=1,stretch_len=5,outline=0)
        self.penup()
        self.goto(position)
        self.setheading(90)


    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)

