from turtle import Turtle , Screen

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

    def move_WS(self):
            self.goto(self.xcor() + 10,   self.ycor() - 10)

    def move_ES(self):
        self.goto(self.xcor() - 10, self.ycor() - 10)

    def move_NW(self):
        self.goto(self.xcor() + 10, self.ycor() + 10)

    def move_NE(self):
        self.goto(self.xcor() - 10, self.ycor() + 10)