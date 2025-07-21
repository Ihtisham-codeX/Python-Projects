from turtle import Turtle , Screen

SPEED = 20

class Paddle(Turtle):

    def __init__(self, x , y):
        super().__init__()
        self.shape("square")
        self.penup()
        self.goto(x,y)
        self.color("white")
        self.shapesize(stretch_len= 1 , stretch_wid= 5)

    def move_up(self):
        if self.ycor() < 235:
            self.goto(self.xcor(), (self.ycor() + SPEED))

    def move_down(self):
        if self.ycor() > -230:
            self.goto(self.xcor(), (self.ycor() - SPEED))







