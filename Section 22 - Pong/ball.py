from turtle import Turtle

MOVE_DISTANCE = 10

class Ball():
    def __init__(self):
        self.ball = Turtle()
        self.ball.penup()
        self.ball.shape("circle")
        self.ball.color("blue")
        self.ball.setheading(30)
        
    def move(self):
        self.ball.forward(MOVE_DISTANCE)