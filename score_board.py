import turtle


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt") as h:
            self.high_score = int(h.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f'score: {self.score} High_score={self.high_score}', move=False, align='center', font=('arial', 25, 'normal'))

        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('highscore.txt', 'w') as h:
                h.write(f"{self.high_score}")                
        self.score = 0
        self.update_scoreboard()


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    
    # def game_over(self):
    #     self.color("red")
    #     self.goto(0, 0)
    #     self.write(f'Game Over...', move=False, align='center', font=('arial', 25, 'normal'))
     