import numpy as np
from utility import *
def main():
    with open("Data Sets\\c_medium.in", 'r') as data:
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
        for y in range(0, R):
            for x in range(0 ,C):
                for i in list(reversed(list(shapes))):
                    potSlice = shapeToSlice((y, x), i)
                    if(isSliceComp(Pmatrix, L, potSlice, R, C) and not checkColision(potSlice, Outputs)):
                        Outputs.append(potSlice)
        print("Outputs", Outputs)
        filledArea = 0
        for tempSlice in Outputs:
            filledArea += (tempSlice[3]-tempSlice[1]+1)*(tempSlice[2]-tempSlice[0]+1)
        print(filledArea, "out of", R*C, "=", filledArea*100/(R*C),"%")

if __name__ == "__main__":
    main()