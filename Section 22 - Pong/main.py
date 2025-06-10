# Imports
from turtle import Turtle
from turtle import Screen
from fence import Fence
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

import time

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

VERTICAL_BOUNDARY = SCREEN_HEIGHT/2 - 25
HORIZONTAL_BOUNDARY = SCREEN_WIDTH / 2
RIGHT_X = HORIZONTAL_BOUNDARY - 35
LEFT_X = -HORIZONTAL_BOUNDARY + 35

RIGHT_PADDLE_STARTING_COORDS = (RIGHT_X, 0)
LEFT_PADDLE_STARTING_COORDS = (LEFT_X, 0)

RIGHT_SCOREBOARD_COORDS = (50 , VERTICAL_BOUNDARY-60)
LEFT_SCOREBOARD_COORDS = (-50, VERTICAL_BOUNDARY-60)

STARTING_GAME_SPEED = 0.1

STARTING_ANGLE = 50

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
ball = Ball(STARTING_ANGLE)
right_scoreboard = Scoreboard(RIGHT_SCOREBOARD_COORDS)
left_scoreboard = Scoreboard(LEFT_SCOREBOARD_COORDS)

screen.update()

# Listen for inputs
screen.listen()
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")

def detect_paddle_collision(paddle):
    time_between_bounces = current_time - ball.last_bounced_time
    if (ball.distance(paddle) < 50 and abs(ball.xcor()) > 340) and time_between_bounces > 0.2:
        ball.bounce("vertical")
        return True
    else:
        return False
            
def detect_wall_collision():
    time_between_bounces = current_time - ball.last_bounced_time
    if (ball.ycor() > VERTICAL_BOUNDARY or ball.ycor() < -VERTICAL_BOUNDARY) and time_between_bounces > 0.2:
        ball.bounce("horizontal")

game_running = True

# Wait a second before starting the ball moving
time.sleep(1)
start_time = time.time()
game_speed = STARTING_GAME_SPEED

while game_running:
    screen.update()
    ball.move()
    time.sleep(game_speed)
    
    current_time = time.time()
    
    if detect_paddle_collision(right_paddle) or detect_paddle_collision(left_paddle):
        game_speed *= 0.9

    # Wall collision
    detect_wall_collision()
    
    # Out of bounds
    if ball.xcor() > HORIZONTAL_BOUNDARY:   # Left scores
        left_scoreboard.increase_score()
    if ball.xcor() < -HORIZONTAL_BOUNDARY: # Right scores
        right_scoreboard.increase_score()
        
        # Pause the game for a sec, then reset the ball
        # time.sleep(2) 
        ball.reset()
        game_speed = STARTING_GAME_SPEED
        time.sleep(1)


screen.exitonclick()