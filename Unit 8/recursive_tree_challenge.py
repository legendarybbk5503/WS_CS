from turtle import *
from random import randint

def drawTree(level, size, angle, ratio):
    if level >= 0:
        forward(size)
        left(angle)
        drawTree(level-1, size/ratio, angle, ratio)

        right(2*angle)

        drawTree(level-1, size/ratio, angle, ratio)
        left(angle)
        forward(-size)
        
    else: return

speed(0)
penup()
goto(0, -220)
left(90)
pendown()

size = 150
angle = 20
ratio = 1.2
level = 10

drawTree(level, size, angle, ratio)