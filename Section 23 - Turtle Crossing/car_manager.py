from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_X_COR = 320
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        cars = []
        self.generate_car()
        # self.create_traffic()
        
        
    # def create_traffic(self):
        # self.generate_car()
        
    def generate_car(self):
        new_car = Turtle()
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.shape("square")
        new_car.shapesize(1,2)
        starting_y = random.randint(-300, 300)
        