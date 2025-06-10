# Imports
from turtle import Turtle
from turtle import Screen
from fence import Fence
from paddle import Paddle
from ball import Ball

import time

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

VERTICAL_BOUNDARY = SCREEN_HEIGHT/2 - 25
HORIZONTAL_BOUNDARY = SCREEN_WIDTH / 2
RIGHT_X = HORIZONTAL_BOUNDARY - 35
LEFT_X = -HORIZONTAL_BOUNDARY + 25

RIGHT_PADDLE_STARTING_COORDS = [(RIGHT_X,30), (RIGHT_X, 10), (RIGHT_X, -10)]
LEFT_PADDLE_STARTING_COORDS = [(LEFT_X,30), (LEFT_X, 10), (LEFT_X, -10)]

# Create the game scene
screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("l e t  u s  p l a y  P O N G")
screen.tracer(0.0)

# Create objects
fence = Fence()
right_paddle = Paddle(RIGHT_PADDLE_STARTING_COORDS)
left_paddle = Paddle(LEFT_PADDLE_STARTING_COORDS)
ball = Ball()

screen.update()

# Listen for inputs
screen.listen()
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")

def detect_paddle_collision(paddle):
    for segment in paddle.segments:
        time_between_bounces = current_time - ball.last_bounced_time
        if segment.distance(ball) < 25 and time_between_bounces > 0.2:
            ball.bounce("vertical")
            
def detect_wall_collision():
    time_between_bounces = current_time - ball.last_bounced_time
    if (ball.ycor() > VERTICAL_BOUNDARY or ball.ycor() < -VERTICAL_BOUNDARY) and time_between_bounces > 0.2:
        ball.bounce("horizontal")

game_running = True

# Wait a second before starting the ball moving
time.sleep(1)
start_time = time.time()

while game_running:
    screen.update()
    ball.move()
    time.sleep(0.05)
    
    current_time = time.time()
    
    detect_paddle_collision(right_paddle)
    detect_paddle_collision(left_paddle)

    # Wall collision
    detect_wall_collision()
    
    # Out of bounds
    if ball.xcor() > HORIZONTAL_BOUNDARY or ball.xcor() < -HORIZONTAL_BOUNDARY:
        pass


screen.exitonclick()