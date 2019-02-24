from math import *

def shapesOfN(H, L):
    #Shapes are stores in (Row, Column) format
    shapes = list()
    tempShapes = list()

    for i in range(1, ceil(sqrt(H))+1):
        for o in range(1, ceil(sqrt(H))+1):
            if i*o<=H and i*o>=L*2:
                    shapes.append((i, o))
                    if(i != o):
                        shapes.append((o, i))

    #ordering shapes by maximum area

    return shapes
