from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, cord: tuple):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.goto(cord)

    # go_up() moves paddle by 20 pixels if below top of screen
    def go_up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    # go_down() moves paddle down by 20 pixel if above bottom of screen
    def go_down(self):
        if self.ycor() > -250:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
