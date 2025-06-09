from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Paddle():
    def __init__(self, starting_coords):
        self.STARTING_COORDS = starting_coords
        self.segments = []
        self.create_paddle()
        self.top_segment = self.segments[0]
        self.bottom_segment = self.segments[-1]
        
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

    def move(self,direction):
        # Depending on the direction, set either the top or the bottom segment as the leading segment
        leading_segment = self.top_segment if direction == UP else self.bottom_segment
        
        # Change coordinates of the trailing segments
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        
        # Move the leading segment
        leading_segment.forward(MOVE_DISTANCE)

    def up(self):
        self.top_segment.setheading(UP)
        self.move(UP)
        
    def down(self):
        self.top_segment.setheading(DOWN)
        self.move(DOWN)
        
   