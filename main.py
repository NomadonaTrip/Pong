from turtle import Turtle, Screen
from paddle import Paddle, PLAYERPOSITION, COMPUTERPOSITION
from ball import Ball, BALLPOSITION
from scoreboard import Score

#Create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

#Create the net to divide the play area into two
linetracer= Turtle()
linetracer.color("white")
linetracer.pensize(5)
linetracer.penup()
linetracer.goto(x=0,y=-300)
linetracer.pendown()
linetracer.setheading(90)
for step in range(30):
    linetracer.pendown()
    linetracer.forward(20)
    linetracer.penup()
    linetracer.forward(20)

linetracer.hideturtle()
# screen.update()



#Create the player and computer paddles
player = Paddle(position = PLAYERPOSITION)
computer = Paddle(position = COMPUTERPOSITION)
ball = Ball()
player_score = Score()
player_score.goto(x= -30, y= 260)
player_score.write_score()
computer_score = Score()
computer_score.goto(x= 30, y= 260)
computer_score.write_score()



screen.update()
screen.tracer(1)

screen.listen()
#player1 controls
screen.onkeypress(fun = player.up, key = "Up")
screen.onkeypress(fun = player.down, key = "Down")

#player2 controls

screen.onkeypress(fun = computer.up, key = "w")
screen.onkeypress(fun = computer.down, key = "s")

def turn():
    in_turn = True
    while in_turn:
        # print(ball.heading())
        ball.move()
        if ball.ycor() < -295 or ball.ycor() > 295:
            ball.bounce()
            # print("wall contact")
        elif ball.xcor() > 360 and ball.distance(player) < 50:
            # print("made contact")
            ball.bounce_y()
        elif ball.xcor() < -360 and ball.distance(computer) < 50:
            ball.bounce_y()
        elif ball.xcor() < -410:
            player_score.add_point()
            in_turn = False
        elif ball.xcor() > 410:
            computer_score.add_point()
            in_turn = False

in_play = True
while in_play:
    ball.goto(x=0, y= 0)
    turn()
    if player_score.score >= 7 or computer_score.score >= 7:
        in_play = False
    else:
        turn()










screen.exitonclick()