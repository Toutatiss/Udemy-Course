from turtle import Turtle
import time

MOVE_DISTANCE = 10

class Ball(Turtle):
    def __init__(self, starting_angle):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("blue")
        self.setheading(starting_angle)
        self.last_bounced_time = 0
        
    def move(self):
        self.forward(MOVE_DISTANCE)
        
    def bounce(self, obstacle_orientation):
        if obstacle_orientation == "vertical":
            new_heading = (180 - self.heading()) % 360 # Mirror the y component, keep with 360 degrees
        elif obstacle_orientation == "horizontal":
            new_heading = (-self.heading()) % 360 # Mirror the x component, keep with 360 degrees
            
        self.setheading(new_heading)
        self.last_bounced_time = time.time()
        
        # print("boing")
        
    def reset(self):
        self.goto(0,0)
        self.bounce("vertical")
        