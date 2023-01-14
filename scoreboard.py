from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    # update_scoreboard() clears score and rewrites score
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 190)
        self.write(self.l_score, align="center", font=("Arial", 80, "normal"))
        self.goto(100, 190)
        self.write(self.r_score, align="center", font=("Arial", 80, "normal"))

    # add_left_score increases left score and calls update_scoreboard
    def add_left_score(self):
        self.l_score += 1
        self.update_scoreboard()

    # add_left_score() increases right score and calls update_scoreboard()
    def add_right_score(self):
        self.r_score += 1
        self.update_scoreboard()