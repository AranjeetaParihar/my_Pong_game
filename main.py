from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Score


screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)
screen.listen()

l_paddle = Paddle(350, 0)
r_paddle = Paddle(-350, 0)

screen.onkey(l_paddle.go_up, 'Up')
screen.onkey(l_paddle.go_down, 'Down')
screen.onkey(r_paddle.go_up, 'w')
screen.onkey(r_paddle.go_down, 's')

pong_ball = Ball()
score = Score()

game_on = True
while game_on:
    screen.update()
    time.sleep(pong_ball.ball_speed)
    pong_ball.move_ball()

    # bounce for the upper and lower wall
    if pong_ball.ycor() > 280 or pong_ball.ycor() < -280:
        pong_ball.y_bounce()

    # bounce when hit the paddle
    if (pong_ball.xcor() > 320 and pong_ball.distance(l_paddle) < 70) or (pong_ball.xcor() < -320 and
                                                                          pong_ball.distance(r_paddle) < 70):
        pong_ball.x_bounce()

        # when right paddle miss
    if pong_ball.xcor() > 380:
        pong_ball.reset_position()
        score.increase_left()
        # when left paddle miss
    if pong_ball.xcor() < -380:
        pong_ball.reset_position()
        score.increase_right()

screen.exitonclick()
