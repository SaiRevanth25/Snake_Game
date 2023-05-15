from turtle import Turtle
FONT = ('Courier', 20, 'normal')
ALIGN = "center"


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(0, 270)
        self.write(f"Score: {self.score} ", align=ALIGN, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score} ", align="center", font=('Arial', 20, 'normal'))

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game Over. Score: {self.score}", align=ALIGN, font=FONT)


