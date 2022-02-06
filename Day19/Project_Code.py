from turtle import Turtle, Screen
import random

# Turtle Racing Game
is_race_on = False
screen = Screen()
screen.setup(width=500, height=600)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "green", "blue", "yellow", "purple", "orange"]
all_turtles = []


x = -100
for turtles in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtles])
    new_turtle.left(90)
    new_turtle.goto(x, -270)
    x += 40
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        if turtle.ycor() > 280:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You've win! The {winning_turtle} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_turtle} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        
screen.exitonclick()
