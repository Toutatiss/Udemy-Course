from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
BOUNDARY = 280

screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Snek")
screen.tracer(0.0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


def reset_game():
    scoreboard.reset_game()
    snake.reset_snake()

game_running = True

while game_running:
    screen.update()
    time.sleep(0.08)
    snake.move()
    
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > BOUNDARY or snake.head.xcor() < -BOUNDARY or snake.head.ycor() > BOUNDARY or snake.head.ycor() < -BOUNDARY:
        reset_game()
        
        
    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            reset_game()

screen.exitonclick()