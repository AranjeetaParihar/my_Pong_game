from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.color('white')
        self.display()

    def increase_left(self):
        self.l_score += 1
        self.clear()
        self.display()

    def increase_right(self):
        self.r_score += 1
        self.clear()
        self.display()

    def display(self):
        self.goto(-50, 240)
        self.write(self.l_score, align='center', font=('courier', 20, 'normal'))
        self.goto(50, 240)
        self.write(self.r_score, align='center', font=('courier', 20, 'normal'))

