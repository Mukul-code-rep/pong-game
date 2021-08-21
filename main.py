import turtle as t
from Paddle import Paddle
from scoreboard import ScoreBoard
from ball import Ball
import time

screen = t.Screen()
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
scoreboard = ScoreBoard()
ball = Ball()

screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

game_on = True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.distance(r_paddle) < 60 and 340 > ball.xcor() > 330) or (ball.distance(l_paddle) < 60 and -340 < ball.xcor() < -330):
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_pos()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_pos()
        scoreboard.r_point()

screen.exitonclick()
