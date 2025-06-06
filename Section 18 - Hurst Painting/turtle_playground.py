import turtle
from turtle import Screen

import random

turtle.colormode(255)

timmy = turtle.Turtle()
timmy.shape("turtle")
timmy.color("orchid")

colours = ["red", "green", "blue", "purple", "pink", "cyan", "yellow"]

def random_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)

# Draw a square
# for _ in range(4):    
#     timmy.forward(100)
#     timmy.right(90)

# # Draw a dashed line
# for _ in range(50):    
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# # Draw shapes
# starting_sides = 3
# for shape in range(7):
#     sides = shape + starting_sides
#     angle = 360/sides
#     timmy.color(random.choice(colours))
#     for _ in range(sides):
#         timmy.forward(50)
#         timmy.right(angle)

# # Random walk
# timmy.pensize(5)
# timmy.speed(10)
# for _ in range(500):
#     direction = 90 * random.randint(0, 3)
#     timmy.color(random_colour())
#     timmy.forward(20)
#     timmy.right(direction)

# Draw Spirograph
size_of_gap = 1
timmy.speed("fastest")
for _ in range(round(360 / size_of_gap)):
    timmy.color(random_colour())
    timmy.circle(100)
    timmy.right(size_of_gap)



screen = Screen()
screen.exitonclick()