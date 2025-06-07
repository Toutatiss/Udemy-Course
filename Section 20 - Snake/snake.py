from turtle import Turtle

STARTING_COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        
    def create_snake(self):
        for position in STARTING_COORDINATES:
            segment = Turtle()
            segment.penup()
            segment.shape("square")
            segment.color("white")
            segment.goto(position)
            self.snake.append(segment)
    
    # Move the snake forward
    def move(self):
        for seg_num in range(len(self.snake)-1,0,-1):
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(new_x,new_y)
        self.snake[0].forward(MOVE_DISTANCE)