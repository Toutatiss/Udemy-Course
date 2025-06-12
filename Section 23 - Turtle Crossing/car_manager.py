from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_X_COR = 320
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.level = 1
        self.generate_car()
        
    def generate_car(self):
        # Appearance
        new_car = Turtle()
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.shape("square")
        new_car.shapesize(1,2)
        
        # Position
        new_car.setheading(180)
        STARTING_Y_COR = random.randint(-300, 300)
        new_car.goto(STARTING_X_COR, STARTING_Y_COR)
        self.cars.append(new_car)
        
    def drive_cars(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE + MOVE_INCREMENT * (self.level - 1))