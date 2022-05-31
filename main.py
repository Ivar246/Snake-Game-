from turtle import Screen, Turtle, exitonclick
import time

screen = Screen()
screen.setup(width=648, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

starting_positions = [(0,0), (-20, 0), (-40, 0)]

segments = []

for position in starting_positions:
    new_segment = Turtle('square')
    new_segment.color('White')
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)


game_is_on = True
while game_is_on:
    screen.update() 
    time.sleep(0.4)
    for seg in segments:
        seg.forward(20)
        
