from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.update_score()
        
    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(self.score, move=False, align=ALIGNMENT, font=FONT)
        
    # def game_over(self):
    #     self.goto(0, 30)
    #     self.write("Game Over!", move=False, align=ALIGNMENT, font=FONT)
        
