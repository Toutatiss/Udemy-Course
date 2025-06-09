from turtle import Turtle

SCREEN_HEIGHT = 600
DASH_LENGTH = 20
NUM_DASHES = SCREEN_HEIGHT/DASH_LENGTH

class Fence(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.pensize(5)
        self.draw_fence()
        
    def draw_fence(self):
        self.penup()
        self.goto(0,300)
        self.setheading(270)
        
        for dash in range(int(NUM_DASHES)):
            self.pendown()
            self.forward(DASH_LENGTH)
            self.penup()
            self.forward(DASH_LENGTH)