from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_X_COR = 320
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        
    def generate_car(self, level):
        # Spawn chance
        CHANCE = 7 - level
        if CHANCE <= 1:
            CHANCE = 1
        if random.randint(1,CHANCE) != 1: # 1 in 6 chance of a car being spawned each tick
            return
        
        # Appearance
        new_car = Turtle()
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.shape("square")
        new_car.shapesize(1,2)
        
        # Position
        new_car.setheading(180)
        STARTING_Y_COR = random.randint(-270, 270)
        new_car.goto(STARTING_X_COR, STARTING_Y_COR)
        self.cars.append(new_car)
          
    def drive_cars(self, level):
        for car in self.cars[:]:  # Iterate over a shallow copy, because removing a car otherwise could cause a car to be missed
            car.forward(STARTING_MOVE_DISTANCE + MOVE_INCREMENT * (level - 1))
            
            # Destroy cars off screen
            if car.xcor() < -340:
                car.hideturtle()
                car.clear()
                self.cars.remove(car)
                del car

    def has_collided(self, player):
        for car in self.cars:
            if car.distance(player) < 20:
                return True
        return False
        