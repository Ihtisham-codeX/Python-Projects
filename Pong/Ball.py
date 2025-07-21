from turtle import Turtle , Screen

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto( 0,-260)

    def move_BR(self):
            self.goto(self.xcor() + 10,   self.ycor() - 10)

    def move_BL(self):
        self.goto(self.xcor() - 10, self.ycor() - 10)

    def move_TR(self):
        self.goto(self.xcor() + 10, self.ycor() + 10)

    def move_TL(self):
        self.goto(self.xcor() - 10, self.ycor() + 10)

    # --------------- Boundary Collision Check Functions For Ball --------------

    def Upper_Boundary_Collision(self):
        if self.ycor() >= 290:
            return True
        return False
    def Lower_Boundary_Collision(self):
        if self.ycor() <= -285:
            return True
        return False
    # --------------- Paddle Collision Check Functions For Ball --------------

    def Paddle_Collision(self , paddle_x , paddle_y ):
        paddle_width = 20
        paddle_length = 68
        ball_x , ball_y = self.position()
        # checking if the ball x coordinate is in the range of paddle x coordinate
        # if abs(ball_x-paddle_x) <= (paddle_width/2) :
        if paddle_x - paddle_width /2 <= ball_x <= paddle_x + paddle_width:
            # checking if the ball y coordinate is in the range of paddle y coordinate
            if paddle_y - paddle_length/2 <= ball_y <= paddle_y + paddle_length:
                return True
        return False









