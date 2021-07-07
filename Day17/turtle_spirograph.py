from turtle import Turtle, Screen
import random

gatsby = Turtle()
gatsby.shape("turtle")
colors = ['red', 'blue', 'green', 'orange', 'yellow', 'violet', 'pink', 'gray']

gatsby.speed('fastest')

def draw_spiro(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        gatsby.circle(100)
        gatsby.color(random.choice(colors))
        gatsby.setheading(gatsby.heading() + size_of_gap)

draw_spiro(4)

screen = Screen()
screen.exitonclick()

