#from math import *

def shapesOfN(n):
    #Shapes are stores in (Row, Column) format
    shapes = list()
    tempShapes = list()
    shapes.append((1, n)) # Basic shapes
    shapes.append((n, 1)) # Vertical and Horizontal Line

    if n%2==0:
        for i in range(2, n, 2):
            for o in range(1, n):
                if i*o<=n:
                    tempShapes.append((i, o))
                    tempShapes.append((o, i))
    else:
        for i in range(2, n-1, 2):
            for o in range(1, n-1):
                if i*o<=n:
                    tempShapes.append((i, o))
                    if(i != o):
                        tempShapes.append((o, i))

    #ordering shapes by maximum area

    for i in reversed(tempShapes):
        shapes.append(i)

    return shapes
