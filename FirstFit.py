import numpy as np

def main():
    with open("Data Sets\\b_small.in", 'r') as data:
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
        print(Pmatrix)


if __name__ == "__main__":
    main()