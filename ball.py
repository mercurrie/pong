from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self. shape("circle")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    # move() sets the goto cordinates for ball
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # bounce_y() flips y direction ball moves
    def bounce_y(self):
        self.y_move *= -1

    # bounce_x() flips x direction ball moves and increases movement speed
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    # reset() resets the ball to start position and flips direction
    def reset(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.1
