import math
import turtle


def square(t, length):
    """Draws a square with sides of the given length.
    Returns the Turtle to the starting position and location.
    """
    for i in range(4):
        t.fd(length)
        t.lt(90)


def polyline(t, n, length, angle):
    """Draws n line segments.
    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(t, n, length):
    """Draws a polygon with n sides.
    t: Turtle
    n: number of sides
    length: length of each side.
    """
    angle = 360.0/n
    polyline(t, n, length, angle)


def arc(t, r, angle):
    """Draws an arc with the given radius and angle.
    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)


def circle(t, r):
    """Draws a circle with the given radius.
    t: Turtle
    r: radius
    """
    arc(t, r, 360)

bob = turtle.Turtle()

radius = 100
bob.pu()
bob.fd(radius)
bob.lt(90)
bob.pd()
circle(bob, radius)

    # wait for the user to close the window
turtle.mainloop()

"""
           |radius     -> 100
           |bob.pu     -> 
__main__   |bob.fd     -> 100
           |bob.lt     -> 90
           |bob.pd     ->

circle     |t          -> bob
           |r          -> 100

           |t          -> bob
           |r          -> 100
           |angle      -> 360
arc        |arc_lenght -> 368.318
           |n          -> 95
           |step_length-> 3.84
           |step_angle -> 3.78
           |t.lt       -> 1.89

           |t          -> bob
           |n          -> 95
polyline   |lenght     -> 3.84
           |angle      -> 3.78
           |t.fd       -> 3.84 |
           |t.lt       -> 3.78 | * n

arc        |t.rt       -> 1.87
 

"""