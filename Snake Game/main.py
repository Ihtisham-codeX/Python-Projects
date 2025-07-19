from turtle import Turtle , Screen
import time
import Snake
import Food
import ScoreBoard
screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.setup(width = 600 , height = 600)
screen.tracer(0)

snake = Snake.Snake()
score = ScoreBoard.ScoreBoard()
food = Food.Food()
screen.listen()

screen.onkey(snake.up , "Up")
screen.onkey(snake.down , "Down")
screen.onkey(snake.left , "Left")
screen.onkey(snake.right , "Right")
while True:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
    if snake.head.xcor() > 290 or snake.head.xcor() < -300 or snake.head.ycor() > 290 or snake.head.ycor() < -290 or (snake.head.position() == snake.tail.position()):
        print("Game Over !")
        break

score.game_end()
screen.exitonclick()







