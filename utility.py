from math import *
import numpy as np
def shapesOfN(H, L, R, C):
    #Shapes are stores in (Row, Column): Area format
    shapes = dict()

    for i in range(1, ceil(sqrt(H))+1):
        for o in range(1, H+1):
            if i*o<=H and i*o>=L*2:
                    if(i<=R and o <= C):
                        shapes[(i, o)] = i*o
                    if(i != o and i<=C and o <= R):
                        shapes[(o, i)] = i*o

    #ordering shapes by min to max area
    sortedList = sorted(shapes, key=shapes.get)
    shapes.clear()
    for i in sortedList:
        shapes[i] = i[0]*i[1]

    return shapes

def checkColision(coordcut, Cutcoordinates):
    #Slice = (R1, C1, R2, C2)
    #returns True on colision
    if len(Cutcoordinates) == 0:
        return False
    for i in coordcut:
        if tuple(i) in Cutcoordinates:
            return True
    #old method
    # for slice in Outputs:
    #     if isOverlaping(Slice, slice):
    #         return True


    return False

def isOverlaping(sliceA, sliceB):
    #slices(Y1 X1 Y2 X2)
    if(sliceA[1]>sliceB[3] or sliceB[1]>sliceA[3]):
        return False
    if(sliceA[0]>sliceB[2] or sliceB[0]>sliceA[2]):
        return False
    return True

def shapeToSlice(topleft, shape):

    return (topleft[0], topleft[1], topleft[0]+shape[0]-1, topleft[1]+shape[1]-1)

def isSliceComp(Matrix, L, Slice, R, C):
    #Checks if a slice is compatible with the matrix rules
    if(Slice[2]>R-1 or Slice[3]>C-1):

        return False
    testSlice = Matrix[Slice[0]:Slice[2]+1, Slice[1]:Slice[3]+1]
    unique, counts = np.unique(testSlice, return_counts=True)
    MT = dict(zip(unique, counts))
    if (MT.get('M') != None and MT.get('T') != None):
        if(MT.get('M')<L or MT.get('T')<L):

            return False
    else:
        return False


    return True

def coorToCut(Cmatrix, Slice, shape):

    return Cmatrix[Slice[0]:Slice[2]+1, Slice[1]:Slice[3]+1].reshape(shape[0]*shape[1],2)

def in1d_broadcast_approach(A,B):
    return A[~((A[:,None,:] == B).all(-1)).any(1)]