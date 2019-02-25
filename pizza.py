from math import *
from functools import reduce

numOfSlices = 0
coordOfSlices = []
occupiedCells = set()
shapes = []
matrix = []
rows = 0
cols = 0
minToppings = 0
maxSize = 0

def factorization(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    a = 1
    return [a] + factors

def pairFactors(n):
    global rows
    global cols
    factors = factorization(n)
    tmp = factors[:]
    dic = {}
    if len(factors) == 1:
        return {}
    elif len(factors) == 2:
        return {(factors[0],factors[1]):factors[0]*factors[1],(factors[1],factors[0]):factors[0]*factors[1]}
    else:
        for idx,valu in enumerate(factors):
            val =factors[idx]
            tmp.pop(idx)
            mul = reduce(lambda x, y: x*y, tmp)
            if val <= rows and val <= cols and mul <= rows and mul <= cols:
                dic[(val,mul)] = mul*val
                dic[(mul,val)] = mul*val
            tmp = factors[:]
    #retdic = sorted(dic)
    return dic
def shapesOfN2(x,y):
    ret = {}
    for i in reversed(range(x,y+1)):
        tmp =  pairFactors(i)
        ret = {**ret, **tmp}
    return ret

def getCoordOfSlices(startPos,shape):
    return (startPos[0],startPos[1],startPos[0]+shape[0]-1,startPos[1]+shape[1]-1)

def takeSlice(startPos,shape):
    global numOfSlices
    global coordOfSlices
    global occupiedCells
    global matrix
    global minToppings

    idxOfShape = allIdxOfShape(startPos,shape)

    outOfBounds = checkOutOfBounds(idxOfShape)
    if outOfBounds:
        print("OutOfbounds")
        return False
    
    hasCol = checkCollisions(shape,startPos,idxOfShape)
    if hasCol:
        print("Collisions")
        return False
    
    (numT,numM) = checkNumberOfTandM(idxOfShape)
    if numT < minToppings or numM < minToppings:
        print("MimumOfToppings")
        return False
    else:
        occupiedCells =   occupiedCells.union(idxOfShape)
        numOfSlices +=1
        coordOfSlices.append(getCoordOfSlices(startPos,shape))
        return True

def allIdxOfShape(startPos,shape):
    idxOfShape =  set()
    print(idxOfShape)
    for i in range(startPos[0],startPos[0]+shape[0]):
       for j in range(startPos[1],startPos[1]+shape[1]):   
           idxOfShape.add((i,j))
    return idxOfShape

def checkOutOfBounds(idxsOfShape):
    global rows
    global cols
    for (i,j) in idxsOfShape:
        if i >= rows or j >=cols:
            return True
    return False

def checkNumberOfTandM(cellsOfSlice):
    global matrix
    numT = 0
    numM = 0
    for (i,j) in cellsOfSlice:
        topping = matrix[i][j]
        if topping == 'T':
            numT+=1
        elif topping == 'M':
            numM+=1
    return (numT,numM)

def checkCollisions(shape,startPos,idxOfShape):
    global occupiedCells

    if len(occupiedCells)==0:
        return False

    commonIdx = idxOfShape.intersection(occupiedCells)

    if len(commonIdx)==0:
        return False
    else:
        return True

def bestFit():
    global matrix
    global minToppings
    global rows
    global cols

    currShape = shapes[0] 
    print(currShape)
    
    for i in range(rows):
        for j in range(cols):
            res = takeSlice((i,j),currShape)
            if res:
                i = i+currShape[0]-1
                j = j+currShape[1]-1

    


def main():
    global matrix
    global minToppings
    global rows
    global cols
    global shapes

    with open("Data Sets\\c_medium.in", 'r') as data:
        firstline = data.readline()
        rows, cols, minToppings, maxSize = [int(i) for i in firstline.split()]
        T = 0
        M = 0
      
        for row in data.readlines():
            temp = list(row)[:-1]
            T += temp.count('T')
            M += temp.count('M')
            matrix.append(temp)

    shapes = list(shapesOfN2(minToppings*2,maxSize).keys())
    
    print(shapes)
    
    for row in matrix:
        print(row)
    
    bestFit()
    """
    res = takeSlice((0,0),(2,2))
    res1 = takeSlice((1,0),(2,2))

    
   
    """
    print("num of slices",numOfSlices)
    print(len(occupiedCells),"out of",rows*cols)
    print("coords",coordOfSlices)

if __name__ == "__main__":
    main()

