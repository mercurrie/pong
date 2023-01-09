import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

direction = 10
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)

paddle_1 = Paddle((350, 0))
paddle_2 = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(paddle_1.go_up, "Up")
screen.onkey(paddle_1.go_down, "Down")
screen.onkey(paddle_2.go_up, "w")
screen.onkey(paddle_2.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move(direction)

    # detect collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()



screen.exitonclick()



# TODO: Create screen
# TODO: Create and move paddles
# TODO: Create another paddle
# TODO: Create ball and move it
# TODO: Detect collison of wall and bounce
# TODO: Detect when paddle misses
# TODO: keep score
