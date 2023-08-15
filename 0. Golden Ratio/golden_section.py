from math import sqrt
from turtle import circle, done, hideturtle, lt, pencolor, pensize, rt, fd, speed

PHI = 2 / (sqrt(5) - 1)


def square(size):
    for _ in range(4):
        fd(size)
        lt(90)


def golden_spiral(n):
    size = 5
    for _ in range(n):
        pencolor('blue')
        square(size)
        pencolor('red')
        circle(size, 90)
        size *= PHI


def print_fibonacci(n):
    a = 1
    b = 1
    for _ in range(n):
        r = b / a
        print(f'{a:15}{b:15}{r:20.16f}')
        a, b = b, a + b


print_fibonacci(40)
print(PHI)
speed('fastest')
hideturtle()
pensize(3)
golden_spiral(9)
done()
