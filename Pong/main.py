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
paddle_1.color("blue")

# Making Player 2 Paddle

paddle_2 = Paddle.Paddle(470,0)
paddle_2.color("red")

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
ball.move_TR()
current_bounce = 2
winner = 0
while True:
    screen.update()
    time.sleep(0.04)

    # ------ Giving Current Bounce , Taking Two Bounces That Can Be Executed
    possible_bounce_1 , possible_bounce_2 = ball.Bounce(current_bounce)

    # ------Setting Current Bounce if collides with wall
    if ball.Lower_Boundary_Collision() or ball.Upper_Boundary_Collision():
        current_bounce = possible_bounce_1

    # ------ Coordinates of paddles
    x1 , y1 = paddle_1.position()
    x2 , y2 = paddle_2.position()

    # ------ Setting Current Bounce if Collides with paddle
    if ball.distance(paddle_2)<50 and ball.xcor() > 440 or ball.distance(paddle_1) < 50 and ball.xcor() < -453:
        current_bounce = possible_bounce_2

    # ------ Increase Score if Collides with right boundary
    if ball.Right_Boundary_Collision():
        Score.increase_p2_score()
        ball.Refresh_Ball()


    # ------ Increase Score If Collides With Left Boundary
    if ball.Left_Boundary_Collision():
        Score.increase_p1_score()
        ball.Refresh_Ball()

    # ------ Moving The Ball According To Current Bounce
    if current_bounce == 1:
        ball.move_TR()
    if current_bounce == 2:
        ball.move_TL()
    if current_bounce == 3:
        ball.move_BL()
    if current_bounce == 4:
        ball.move_BR()

    # ------ Declaring Winner Who Scores 5 first
    if Score.p1_score == 5:
        winner = 1
        break
    if Score.p2_score == 5:
        winner = 2
        break


if winner == 2:
    Score.show_winner_text("blue", "BLUE WINS!")
    ball.hideturtle()
    screen.update()  # because tracer(0)
    screen.exitonclick()

if winner == 1:
    Score.show_winner_text("red", "RED WINS!")
    ball.hideturtle()
    screen.update()
    screen.exitonclick()

