from turtle import Turtle
from turtle import Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("orchid")

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

starting_sides = 3
# Draw triangle
for shape in range(7):
    sides = shape + starting_sides
    angle = 360/sides
    for _ in range(sides):
        timmy.forward(50)
        timmy.right(angle)

# Draw shapes
# for shapes in range(7):
#     for sides in :    
#         timmy.forward(20)
    





screen = Screen()
screen.exitonclick()