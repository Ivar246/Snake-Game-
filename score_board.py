import turtle


class Scoreboard(turtle.Turtle):
    def __init__(self):
        self.score = 0
        self.color("white")
        self.write(f'score: {self.score}', move=False, align='center', font=('arial', 25, 'normal'))