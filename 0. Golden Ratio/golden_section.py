from math import sqrt
from turtle import circle, done, hideturtle, lt, pencolor, pensize, rt, fd, speed

PHI = 2 / (sqrt(5) - 1)

def square(size):
    for _ in range(4):
        fd(size)
        lt(90)


print(PHI)

def golden_spiral(n):
    size = 5
    for _ in range(n):
        pencolor('blue')
        square(size)
        pencolor('red')
        circle(size, 90)
        size *= PHI

speed('fastest')
hideturtle()
pensize(3)
golden_spiral(9)
done()
