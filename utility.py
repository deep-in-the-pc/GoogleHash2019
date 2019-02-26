from math import *
import numpy as np
import matplotlib.pyplot as plt

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

def exportOutputs(inputString, Outputs):
    nSlices = len(Outputs)
    outputString = inputString[:-2] + "out"
    with open(outputString, 'w') as outfile:
        outfile.write(str(nSlices)+"\n")
        for i in Outputs:
            outfile.write(str(i[0])+" "+str(i[1])+" "+str(i[2])+" "+str(i[3])+"\n")


def show_output(fname):
    """Reads an output file, assuming it's valid and plots the result."""
    input_fname = fname.split('.')[0] + '.in'
    R, C, L, H, pizza = read_input_pizza(input_fname)
    lines = open(fname).readlines()
    N = int(lines[0].strip())
    slice_mask = np.zeros_like(pizza)
    pizza_slices = []
    for i in range(1, N + 1):
        r, c, dr, dc = [int(val) for val in lines[i].strip().split()]
        dr += 1 - r
        dc += 1 - c
        slice_mask[r:r + dr, c:c + dc] = i
        pizza_slices.append([r, c, dr, dc])

    fig, axes = plt.subplots(figsize=(9, 4), ncols=2, sharex=True, sharey=True)
    axes[0].imshow(slice_mask)
    axes[0].set_title(f'coloring by slice number (1 to {slice_mask.max()})')

    axes[1].imshow((slice_mask > 0).astype(np.int))
    axes[1].set_title('coloring by empty (green) / occupied (yellow)')

    plt.suptitle(f'solution score: {score(pizza_slices)}')
    plt.tight_layout(rect=[0, 0, 1, .95])

    axes[1].axis((-.5, C - .5, R - .5, -.5))

    plt.show()

def read_input_pizza(filename):
    """Reads the input of a Pizza problem.

    returns:

    R: number of Rows of pizza grid
    C: number of Cols of pizza grid
    L: Lowest number of each ingredients per slice
    H: Highest number of cells per slice
    pizza: the pizza grid (1 == tomato, 0 == mushroom)
    """
    lines = open(filename).readlines()
    R, C, L, H = [int(val) for val in lines[0].split()]
    pizza = np.array([list(map(lambda item: 1 if item == 'T' else 0, row.strip())) for row in lines[1:]])
    return R, C, L, H, pizza

def score(pizza_slices):
    """Computes score of given pizza_slices list."""
    s = 0
    for pizza_slice in pizza_slices:
        s += pizza_slice[2] * pizza_slice[3]
    return s
