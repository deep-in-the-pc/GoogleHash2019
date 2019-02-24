from math import *

def shapesOfN(H, L):
    #Shapes are stores in (Row, Column): Area format
    shapes = dict()

    for i in range(1, ceil(sqrt(H))+1):
        for o in range(1, H+1):
            if i*o<=H and i*o>=L*2:
                    shapes[(i, o)] = i*o
                    if(i != o):
                        shapes[(o, i)] = i*o

    #ordering shapes by min to max area
    sortedList = sorted(shapes, key=shapes.get)
    shapes.clear()
    for i in sortedList:
        shapes[i] = i[0]*i[1]

    return shapes
