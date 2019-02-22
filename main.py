from math import *

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

    shapes.append(list(reversed(tempShapes)))

    return shapes

def compatibilitySearch(matrix, shape):
    #Returns list of x1, y1, x2, y2 coordinates for slices
    slices = list()



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
    print("")
    #Basic Info
    print("\n")
    print("R C L H T  M")
    print(R, C, L, H, T, M)



    print("Possible Shapes =", shapesOfN(H))

    for row in Pmatrix:
        print(row)

if __name__ == "__main__":
    main()