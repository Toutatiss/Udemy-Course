# Turtle Race
from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Choose a colour: ")

timmy = Turtle()

screen.exitonclick()