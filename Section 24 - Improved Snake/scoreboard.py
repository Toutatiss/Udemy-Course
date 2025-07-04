from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.read_high_score()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_score()
        
    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)
        
    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score()
        self.score = 0
        self.update_score()
        
    def read_high_score(self):
        with open("/Users/felka/Documents/Python/Udemy Course/Section 24 - Improved Snake/score.txt", "r") as score_file:
            self.high_score = int(score_file.read())
    
    def write_high_score(self):
        with open("/Users/felka/Documents/Python/Udemy Course/Section 24 - Improved Snake/score.txt", "w") as score_file:
            score_file.write(str(self.high_score))
        
