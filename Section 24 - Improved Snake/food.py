from turtle import Turtle
import random

COORD_LIMIT = 280

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
        
    def refresh(self):
        random_x = random.randint(-COORD_LIMIT, COORD_LIMIT)
        random_y = random.randint(-COORD_LIMIT, COORD_LIMIT)
        self.goto(random_x, random_y)