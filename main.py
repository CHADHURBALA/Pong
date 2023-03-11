from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

p_1 = Paddle((350, 0))
p_2 = Paddle((-350, 0))
ball = Ball()
score = ScoreBoard()

screen.listen()
screen.onkey(p_1.go_up, "Up")
screen.onkey(p_1.go_down, "Down")
screen.onkey(p_2.go_up, "w")
screen.onkey(p_2.go_down, "s")

is_on = True

while is_on:
    time.sleep(ball.speed)
    screen.update()
    ball.move()
    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # with right paddle
    if ball.distance(p_1) < 50 and ball.xcor() > 320 or ball.distance(p_2) < 50 and ball.xcor() < - 320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset()
        score.l_point()
    if ball.xcor() < -380:
        ball.reset()
        score.r_point()


screen.exitonclick()
