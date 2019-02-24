from math import *
from utility import *

def compatibilitySearch(matrix, shape):
    #Returns list of x1, y1, x2, y2 coordinates for slices
    slices = list()
    T = 0
    M = 0



    return slices

def main():
    with open("Data Sets\\b_small.in", 'r') as data:
        firstline = data.readline()
        R, C, L, H = [int(i) for i in firstline.split()]
        T = 0
        M = 0
        Pmatrix = []
        for row in data.readlines():
            temp = list(row)[:-1]
            T += temp.count('T')
            M += temp.count('M')
            Pmatrix.append(temp)

    if(T < M):
        min_s = ceil(T/L)
    else:
        min_s = ceil(M/L)

    max_s = ceil(R*C/H)
    print("Max number of slices by pieces = " + str(min_s))
    print("Min number of slices by biggest slice = " + str(max_s))
    #Basic Info
    print("\n")
    print("R C L H T  M")
    print(R, C, L, H, T, M)



    print("Possible Shapes =", shapesOfN(12, L))

    for row in Pmatrix:
        print(row)

if __name__ == "__main__":
    main()