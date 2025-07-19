from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.scoreboard = 0
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.write(f"Score : {self.scoreboard}" ,align = "center" , font = ("Arial" , 24 , "normal"))
        self.hideturtle()
    def increase_score(self):
        self.scoreboard+=1
        self.clear()
        self.write(f"Score : {self.scoreboard}" ,align = "center" , font = ("Arial" , 24 , "normal"))

    def game_end(self):
        self.color("white")
        self.goto(0,20)
        self.write("Game Over !" ,align = "center" , font = ("Arial" , 18 , "normal"))
