from turtle import Turtle

MOVE_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self, starting_coords):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.goto(starting_coords)

    def up(self):
        if self.ycor() < 300:
            self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)
        
    def down(self):
        if self.ycor() > -300:
            self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)
        
   