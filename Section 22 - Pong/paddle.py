from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Paddle(Turtle):
    def __init__(self, starting_coords):
        self.STARTING_COORDS = starting_coords
        self.xcor = starting_coords[0][0]
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
        # Idendify leading segment, and define loop order and increment direction
        if direction == UP:
            leading_segment = self.top_segment
            segment_order = range(len(self.segments)-1,0,-1)
            seg_increment = -1
        elif direction == DOWN:
            leading_segment = self.bottom_segment
            segment_order = range(0, len(self.segments)-1)
            seg_increment = 1
            
        for seg_num in segment_order:
            new_y = self.segments[seg_num + seg_increment].ycor()
            self.segments[seg_num].goto(self.xcor,new_y)
        
        # Move the leading segment
        leading_segment.forward(MOVE_DISTANCE)

    def up(self):
        self.top_segment.setheading(UP)
        self.move(UP)
        
    def down(self):
        self.bottom_segment.setheading(DOWN)
        self.move(DOWN)
        
   