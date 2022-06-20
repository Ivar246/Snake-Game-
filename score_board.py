import turtle


class Scoreboard(turtle.Turtle):
    def __init__(self, score):
        self.clear()
        self.write(f'score: {self.score}', move=False, align='center', font=('arial', 25, 'normal'))