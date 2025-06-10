# Imports
from turtle import Turtle
from turtle import Screen
from fence import Fence
from paddle import Paddle
from ball import Ball

import time

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

RIGHT_PADDLE_STARTING_COORDS = [(280,30), (280, 10), (280, -10)]
LEFT_PADDLE_STARTING_COORDS = [(-290,30), (-290, 10), (-290, -10)]

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

game_running = True

# Wait a second before starting the ball moving
time.sleep(1)

while game_running:
    screen.update()
    ball.move()
    time.sleep(0.05)

screen.exitonclick()