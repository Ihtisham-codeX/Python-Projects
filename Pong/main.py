from turtle import Screen , Turtle
import Paddle
import Score
import time
import Ball

# --------------------------  Adding Screen  --------------------------
screen = Screen()
screen.setup( width = 1000 , height = 600)
screen.bgcolor("black")
# Disabling the step by step drawing on screen
screen.tracer(0)

# ----------------------- Adding Objects On Screen  -----------------------

# making verticel center line

line = Turtle()
line.hideturtle()
line.color("white")
y = 264
line.penup()
line.goto(0,y)
line.setheading(270)
for dot in range(60):
    line.dot(6)
    line.forward(10)

# Making The player 1 Paddle

paddle_1 = Paddle.Paddle(-483,0)

# Making Player 2 Paddle

paddle_2 = Paddle.Paddle(470,0)

# Adding Score On Top

Score = Score.Score()

# Adding Ball

ball = Ball.Ball()

# Enabling the Drawing on screen at once
screen.update()

# -----------------------  Key Workings  -----------------------

screen.listen()
screen.onkeypress(paddle_1.move_up , "w")
screen.onkeypress(paddle_1.move_down , "s")
screen.onkeypress(paddle_2.move_up , "Up")
screen.onkeypress(paddle_2.move_down , "Down")

# -------------------------- Game Loop  --------------------------
while True:
    screen.update()
    ball.move_TL()
    time.sleep(0.04)
    if ball.Lower_Boundary_Collision() or ball.Upper_Boundary_Collision():
        break
    x1 , y1 = paddle_1.position()
    x2 , y2 = paddle_2.position()
    if ball.Paddle_Collision(x2 , y2) or ball.Paddle_Collision(x1 , y1):
        break


# Exit On Click
screen.exitonclick()