from turtle import Turtle

FONT = ("Courier", 24, "normal")
POSITION = (-270, 260)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(POSITION)
        self.update_level()
        
    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}", move=False, align="left", font=FONT)
        
    def increase_level(self):
        self.level += 1
        self.update_level()
        
    def game_over(self):
        self.goto(0,0)
        self.write("Game over!", move=False, align="center", font=FONT)
        
