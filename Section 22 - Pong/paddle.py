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
        # Identify which is the first segment
        if direction == UP: # The top segment is leading (first one in the array)
            leading_segment = self.top_segment
            for seg_num in range(len(self.segments)-1,0,-1):
                new_x = self.segments[seg_num - 1].xcor()
                new_y = self.segments[seg_num - 1].ycor()
                self.segments[seg_num].goto(new_x,new_y)
        elif direction == DOWN:
            leading_segment = self.bottom_segment
            for seg_num in range(0, len(self.segments)-1):
                new_x = self.segments[seg_num + 1].xcor()
                new_y = self.segments[seg_num + 1].ycor()
                self.segments[seg_num].goto(new_x,new_y)
        
        # Move the leading segment
        leading_segment.forward(MOVE_DISTANCE)

    def up(self):
        self.top_segment.setheading(UP)
        self.move(UP)
        
    def down(self):
        self.bottom_segment.setheading(DOWN)
        self.move(DOWN)
        
   