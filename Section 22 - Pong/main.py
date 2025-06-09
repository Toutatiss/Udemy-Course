# Imports
from turtle import Turtle
from turtle import Screen
from paddle import Paddle
from fence import Fence

import time

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Create the game scene
screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("grey")
screen.title("l e t  u s  p l a y  P O N G")
screen.tracer(0.0)

# Create objects
fence = Fence()
screen.update()

right_paddle = Paddle()
# left_paddle = Paddle()

# # Listen for inputs
# screen.listen()
# screen.onkey(right_paddle.up, "Up")
# screen.onkey(right_paddle.down, "Down")
# screen.onkey(left_paddle.up, "W")
# screen.onkey(left_paddle.down, "S")

# game_running = True

# while game_running:
#     screen.update()
#     time.sleep(0.08)

screen.exitonclick()