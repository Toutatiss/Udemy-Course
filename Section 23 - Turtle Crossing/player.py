from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        # Create turtle
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        
        # Other varianbles
        self.level = 1
        
    def move_forward(self):
        self.forward(MOVE_DISTANCE)
            
    def is_at_finish_line(self):
        if self.ycor() >= FINISH_LINE_Y:
            # Return to the start
            self.goto(STARTING_POSITION)
            self.level += 1
            return True
        else:
            return False
        
            
        