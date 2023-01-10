from turtle import Turtle

BALL_SHAPE = "circle"
BALL_COLOR = "white"
BALL_WIDTH = 1
BALL_LEN = 1
BALL_MOVE_SPEED = 0.1
SPEED_INCREMENT = 0.9
BALL_START_POSITION = (0, 0)
FLIP_DIRECTION = -1
BALL_MOVE_DISTANCE = 10


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self. shape(BALL_SHAPE)
        self.penup()
        self.shapesize(BALL_WIDTH, BALL_LEN)
        self.color(BALL_COLOR)
        self.x_move = BALL_MOVE_DISTANCE
        self.y_move = BALL_MOVE_DISTANCE
        self.move_speed = BALL_MOVE_SPEED

    # move() sets the goto cordinates for ball
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # bounce_y() flips y direction ball moves
    def bounce_y(self):
        self.y_move *= FLIP_DIRECTION

    # bounce_x() flips x direction ball moves and increases movement speed
    def bounce_x(self):
        self.x_move *= FLIP_DIRECTION
        self.move_speed *= SPEED_INCREMENT

    # reset() resets the ball to start position and flips direction
    def reset(self):
        self.goto(BALL_START_POSITION[0], BALL_START_POSITION[1])
        self.bounce_x()
        self.move_speed = BALL_MOVE_SPEED
