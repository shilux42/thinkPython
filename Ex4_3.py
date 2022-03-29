import turtle, math
bob = turtle.Turtle()

def square(t, lenght):
    """t: the drawing turtle
       lenght: the side l """
    for i in range(4):
        t.fd(lenght)
        t.rt(90)

def polyline(t, n, lenght, angle):
    """t: the drawing turtle
       lenght: the side l 
       n: number of angles
       angle: the angle of sides"""
    for i in range(n):
        t.fd(lenght)
        t.rt(angle)

def poligon(t, n, lenght):
    """t: the drawing turtle
       lenght: the side l 
       n: number of angles"""
    angle = 360 / n
    polyline(t, n, lenght, angle)


def arc(t, r, angle):
    """t: the draving turtle
       r: the radius of arc
       angle: the fraction of the circle to draw"""
    arcLenght = 2 * math.pi * r * angle / 360
    n = int(arcLenght / 3) + 1
    stepLenght = arcLenght / n
    stepAngle = angle / n
    polyline(t, n, stepLenght, stepAngle)

def circle(t, r):
    arc(t, r, 360)

circle(bob, 100)

turtle.mainloop()