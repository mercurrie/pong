import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TITLE = "Pong"
SCREEN_COLOR = "black"
ANIMATION_OFF = 0
RIGHT_PADDLE_START_POSITION = (350, 0)
RIGHT_PADDLE_UP = "Up"
RIGHT_PADDLE_DOWN = "Down"
LEFT_PADDLE_START_POSITION = (-350, 0)
LEFT_PADDLE_UP = "w"
LEFT_PADDLE_DOWN = "s"
BALL_WALL_COLLISION = 280
BALL_PADDLE_COLLISION = 40
MISS_DISTANCE = 380
HIT_DISTANCE = 320

screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.title(TITLE)
screen.bgcolor(SCREEN_COLOR)
screen.tracer(ANIMATION_OFF)

right_paddle = Paddle(RIGHT_PADDLE_START_POSITION)
left_paddle = Paddle(LEFT_PADDLE_START_POSITION)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.go_up, RIGHT_PADDLE_UP)
screen.onkey(right_paddle.go_down, RIGHT_PADDLE_DOWN)
screen.onkey(left_paddle.go_up, LEFT_PADDLE_UP)
screen.onkey(left_paddle.go_down, LEFT_PADDLE_DOWN)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # detect collision with walls
    if ball.ycor() > BALL_WALL_COLLISION or ball.ycor() < -BALL_WALL_COLLISION:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(right_paddle) < BALL_PADDLE_COLLISION and ball.xcor() > HIT_DISTANCE or \
            ball.distance(left_paddle) < BALL_PADDLE_COLLISION and ball.xcor() < HIT_DISTANCE:
        ball.bounce_x()

    # detect if R paddle misses
    if ball.xcor() > MISS_DISTANCE:
        ball.reset()
        scoreboard.add_left_score()

    # detect if L paddle misses
    if ball.xcor() < -MISS_DISTANCE:
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
