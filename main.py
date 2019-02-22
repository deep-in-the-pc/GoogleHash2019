from math import *

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
print(Pmatrix)
for row in Pmatrix:
    print(row)