from turtle import Turtle
PADDLE_WIDTH = 5
PADDLE_LEN = 1
PADDLE_SHAPE = "square"
PADDLE_COLOR = "white"
MOVE_INCREMENT = 20
SCREEN_BOUNDARY = 250


class Paddle(Turtle):

    def __init__(self, cord: tuple):
        super().__init__()
        self.penup()
        self.shape(PADDLE_SHAPE)
        self.shapesize(PADDLE_WIDTH, PADDLE_LEN)
        self.color(PADDLE_COLOR)
        self.goto(cord)

    # go_up() moves paddle by 20 pixels if below top of screen
    def go_up(self):
        if self.ycor() < SCREEN_BOUNDARY:
            new_y = self.ycor() + MOVE_INCREMENT
            self.goto(self.xcor(), new_y)

    # go_down() moves paddle down by 20 pixel if above bottom of screen
    def go_down(self):
        if self.ycor() > -SCREEN_BOUNDARY:
            new_y = self.ycor() - MOVE_INCREMENT
            self.goto(self.xcor(), new_y)
