import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

player = Player()
car_manager = CarManager()

# Listen for key presses
screen.listen()
screen.onkey(player.move_forward, "Up")

game_is_on = True
while game_is_on:
    car_manager.drive_cars()
    
    time.sleep(0.1)
    screen.update()
    
