def beam():
    print('+', '- ' * 4, end='')

def doTwice(f):
    f()
    f()

def doFour(f):
    doTwice(f)
    doTwice(f)

def laserBeam():
    doFour(beam)
    print('+')

def segment():
    print('|', ' ' * 7, end=' ')
    
def column():
    doFour(segment)
    print('|')

def halfSquare():
    laserBeam()
    doFour(column)

def grid4x4():
    doFour(halfSquare)
    laserBeam()

grid4x4()

