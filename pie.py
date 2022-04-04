import turtle, math
bob = turtle.Turtle()

def pie(t, r, n):
    """t: drawing turtle
           r: the radius/sides of the pie/slices
           n: numerbers of slice
           """
    alpha = 360 / n
    beta = math.radians((180 - alpha) / 2)
    base = 2 * r * math.cos(beta)
    betaDegrees = math.degrees(beta)
    
    for i in range(n):
        t.fd(r)
        t.rt(180 - betaDegrees)
        t.fd(base)
        t.rt(180 - betaDegrees)
        t.fd(r)
        t.lt(180)

def move(d):
    """d: distance"""
    bob.pu()
    bob.fd(d)
    bob.pd()

move(-250)
pie(bob, 100, 5)
move(250)
pie(bob, 100, 7)
move(250)
pie(bob, 100, 9)


turtle.mainloop()
