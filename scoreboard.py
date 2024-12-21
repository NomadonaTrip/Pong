from turtle import Turtle, Screen
FONT = ("courier", 30, "normal" )
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.score = 0
        self.hideturtle()

    def write_score(self):
        self.write(self.score, align="center", font=FONT)

    def add_point(self):
        self.clear()
        self.score += 1
        self.write_score()
        # self.showturtle()

    def game_over(self):
        self.write("Game over")

