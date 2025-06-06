import colorgram
import turtle
import random

turtle.colormode(255)

timmy = turtle.Turtle()
colors = colorgram.extract('/Users/felka/Documents/Python/Udemy Course/Section 18 - Hurst Painting/image.jpg', 85) 
colors.remove(colors[0]) # Get rid of the background colour

# Turtle position setup
timmy.teleport(-270, -270)
timmy.speed("fastest")

## My Attempt
# going_right = True
# # Draw first dot
# timmy.color(random.choice(colors).rgb)
# timmy.forward(1)

# # Draw Row
# for row in range(6):
#     for row_dot in range(5):
#         timmy.color(random.choice(colors).rgb)
#         timmy.penup()
#         timmy.forward(100)
#         timmy.pendown()
#         timmy.forward(1)
#     if row != 5:
#         timmy.penup()
#         timmy.setheading(90)
#         timmy.forward(99)
#         timmy.pendown()
#         timmy.forward(1)
#     if going_right:
#         going_right = False
#         timmy.setheading(180)
#     else:
#         going_right = True
#         timmy.setheading(0)

## New Attempt
timmy.penup()
timmy.hideturtle()
number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):
    timmy.dot(20, random.choice(colors).rgb)
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)
        
screen = turtle.Screen()
screen.exitonclick()
