import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

direction = 10
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # detect collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect if R paddle misses
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.add_left_score()

    # detect if L paddle misses
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.add_right_score()

screen.exitonclick()

# TODO: Create screen
# TODO: Create and move paddles
# TODO: Create another paddle
# TODO: Create ball and move it
# TODO: Detect collision of wall and bounce
# TODO: Detect when paddle misses
# TODO: keep score
