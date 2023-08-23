from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()
timmy.shape("circle")
timmy.speed(0)
screen.colormode(255)
a = 5
while a <= 360:
    R = random.randint(1, 255)
    G = random.randint(1, 255)
    B = random.randint(1, 255)
    timmy.color(R, G, B)
    timmy.circle(100)
    timmy.setheading(a)
    a += 5

screen.exitonclick()
