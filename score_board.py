import turtle


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.write(f'score: {self.score}', move=False, align='center', font=('arial', 25, 'normal'))


    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f'score: {self.score}', move=False, align='center', font=('arial', 25, 'normal'))

    
    def game_over(self):
        self.color("red")
        self.goto(0, 0)
        self.write(f'Game Over...', move=False, align='center', font=('arial', 25, 'normal'))