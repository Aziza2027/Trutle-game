from turtle import Turtle

FONT = ("Courier", 20, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.write(f'Level: {self.level}', font = FONT)

    def update(self):
        self.level += 1
        self.clear()
        self.write(f'Level: {self.level}', font = FONT)