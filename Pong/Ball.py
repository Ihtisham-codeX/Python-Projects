from turtle import Turtle , Screen
SPEED = 10

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto( 0,-260)

    def move_BR(self):
            self.goto(self.xcor() + SPEED,   self.ycor() - SPEED)

    def move_BL(self):
        self.goto(self.xcor() - SPEED, self.ycor() - SPEED)

    def move_TR(self):
        self.goto(self.xcor() + SPEED, self.ycor() + SPEED)

    def move_TL(self):
        self.goto(self.xcor() - SPEED, self.ycor() + SPEED)

    def Refresh_Ball(self):
        self.goto(0,0)

    # --------------- Boundary Collision Check Functions For Ball --------------

    def Upper_Boundary_Collision(self):
        if self.ycor() >= 290:
            return True
        return False
    def Lower_Boundary_Collision(self):
        if self.ycor() <= -285:
            return True
        return False

    def Right_Boundary_Collision(self):
        if self.xcor() >= 500:
            return True
        return False

    def Left_Boundary_Collision(self):
        if self.xcor() <= -500:
            return True
        return False
    # --------------- Paddle Collision Check Functions For Ball --------------

    def Paddle_Collision(self , paddle_x , paddle_y ):
        paddle_width = 20
        paddle_length = 90
        ball_x , ball_y = self.position()
        # checking if the ball x coordinate is in the range of paddle x coordinate
        # if abs(ball_x-paddle_x) <= (paddle_width/2) :
        if paddle_x - paddle_width /2 <= ball_x <= paddle_x + paddle_width:
            # checking if the ball y coordinate is in the range of paddle y coordinate
            if paddle_y - paddle_length/2 <= ball_y <= paddle_y + paddle_length:
                return True
        return False
    # --------- Making a function that tells which side the ball bounces ------

    def Bounce(self , Prev_Bounce):
        if Prev_Bounce == 1:
            return 4 , 2
        elif Prev_Bounce == 2:
            return 3 , 1
        elif Prev_Bounce == 3:
            return 2 , 4
        elif Prev_Bounce == 4:
            return 1 , 3
        return 0








