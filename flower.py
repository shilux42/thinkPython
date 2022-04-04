import turtle, math
import polygon

bob = turtle.Turtle()


def petal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        t.rt(180 - angle)

def flower(t, r, angle, petals):
    for i in range(petals):
        petal(t, r, angle)
        t.rt(360 / petals)

def move(d):
    #d is the distance
    bob.pu()
    bob.fd(d)
    bob.pd()

move(-250)
flower(bob, 100, 50, 8)
move(250)
flower(bob, 80, 80, 10)
move(250)
flower(bob, 70, 80, 20)

turtle.mainloop()