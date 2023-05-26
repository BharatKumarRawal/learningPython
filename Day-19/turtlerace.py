import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which color turtle will win the race: ")
print(user_bet)
y_cord = [-78, -48, -18, 8, 38, 68]
all_turtles = []
if user_bet:
    is_race_on = True

for turtle_index in range(0, 6):
    new_tut = Turtle(shape="turtle")
    new_tut.color(colors[turtle_index])
    new_tut.penup()
    new_tut.goto(x=-230, y=y_cord[turtle_index])
    all_turtles.append(new_tut)

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Congratulations You won! {winning_color} turtle won the game")
            else:
                print(f"Sorry You loose! {winning_color} turtle won the game")

        distancee = random.randint(0, 10)
        turtle.forward(distancee)

screen.exitonclick()
