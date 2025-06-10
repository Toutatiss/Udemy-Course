from turtle import Turtle
import time

MOVE_DISTANCE = 10

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("blue")
        self.setheading(30)
        self.last_bounced_time = 0
        
    def move(self):
        self.forward(MOVE_DISTANCE)
        
    def bounce(self, obstacle_orientation):
        if obstacle_orientation == "vertical":
            new_heading = (180 - self.heading()) % 360
        elif obstacle_orientation == "horizontal":
            new_heading = (-self.heading()) % 360
            
        self.setheading(new_heading)
        self.last_bounced_time = time.time()
        
        # print("boing")
        