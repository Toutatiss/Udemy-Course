from turtle import Turtle

PADDLE_LENGTH = 3

class Paddle():
    def __init__(self, starting_coords):
        self.STARTING_COORDS = starting_coords
        self.segments = []
        self.create_paddle()
        
    def add_segment(self, position):
        segment = Turtle()
        segment.penup()
        segment.shape("square")
        segment.color("white")
        segment.goto(position)
        self.segments.append(segment)
        
    def create_paddle(self):
        for position in self.STARTING_COORDS:
           self.add_segment(position)
       


    # Draw paddle on the screen
        # It needs to be 3 white, square turtles linked together
        # Take an input to decide where the paddle should be drawn first
        
    # Move the paddle
        # Make a function for up and down