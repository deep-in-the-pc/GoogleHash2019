import numpy as np
import time
from utility import *
import itertools

def main():
    input = "Data Sets\\c_medium.in"
    t0 = time.time()
    with open(input, 'r') as data:
        firstline = data.readline()
        R, C, L, H = [int(i) for i in firstline.split()]
        T = 0
        M = 0
        Pmatrix = np.empty((0, C), dtype=np.dtype('U'))
        i = 0
        for row in data.readlines():
            temp = list(row)[:-1]
            tempArray = np.array(list(row)[:-1])
            Pmatrix = np.append(Pmatrix, [tempArray], axis=0)
            T += temp.count('T')
            M += temp.count('M')
            i+=1
        Outputs = list()
        shapes = shapesOfN(H, L, R, C)
        print(R, C, L, H, T, M)
        print(Pmatrix)
        print("\nPossible Shapes:", shapes)

        # Faster but less effective

    Row = np.arange(int(R))
    Col = np.arange(int(C))

    out = list(itertools.product(Row, Col))

    out.sort(key=lambda x: x[0])

    Cmatrix = np.array(out).reshape(int(R),int(C),2)

    Carray = Cmatrix.reshape(int(R)*int(C), 2)
    Cutcoords = set()

    n = 0
    while(n<C*R):
        if tuple(Carray[n]) in Cutcoords:
            n+=1
            continue
        for i in list(reversed(list(shapes))):
            potSlice = shapeToSlice((Carray[n][0], Carray[n][1]), i)
            if isSliceComp(Pmatrix, L, potSlice, R, C ):
                coordcut = coorToCut(Cmatrix, potSlice, i)
                if not checkColision(coordcut, Cutcoords):
                    Outputs.append(potSlice)
                    coordcut_hash = map(tuple, coordcut)
                    for x in coordcut_hash:
                        Cutcoords.add(x)
                    break
        n+=1


    t1 = time.time()
    #Stats
    print("Outputs", Outputs)
    filledArea = 0
    for tempSlice in Outputs:
        filledArea += (tempSlice[3]-tempSlice[1]+1)*(tempSlice[2]-tempSlice[0]+1)
    print(filledArea, "out of", R*C, "=", filledArea*100/(R*C),"%", "in",t1-t0,"s")

    exportOutputs(input, Outputs)
    show_output(input[:-2] + "out")

if __name__ == "__main__":
    main()