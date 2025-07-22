from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.p1_score = 0
        self.p2_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.write(f"{self.p2_score} : Score : {self.p1_score}", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()

    def increase_p1_score(self):
        self.p1_score += 1
        self.clear()
        self.write(f"{self.p2_score} : Score : {self.p1_score}", align="center", font=("Arial", 24, "normal"))

    def increase_p2_score(self):
        self.p2_score += 1
        self.clear()
        self.write(f"{self.p2_score} : Score : {self.p1_score}", align="center", font=("Arial", 24, "normal"))

    def show_winner_text(self , color_name, text):
        writer = Turtle()
        writer.hideturtle()
        writer.penup()
        writer.color(color_name)
        writer.goto(0, 0)
        writer.write(text, align="center", font=("Courier", 36, "bold"))

