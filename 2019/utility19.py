import numpy as np

class Photo():
    def __init__(self, id, o, nT, tagsS, tagsL):
        self.id = id
        self.Orientation = o
        self.nTags = nT
        self.tagsS = tagsS
        self.tagsL = tagsL



def readInput(inputFile):
    inputPath = "Data Sets\\"+inputFile+".txt"
    with open(inputPath, 'r') as data:
        photos = list()
        firstline = data.readline()
        N = int(firstline)
        n = 0
        for row in data.readlines():
            line = row.split()
            O = line[0]
            nT = int(line[1])
            tagsL = [i for i in line[2:]]
            tagsS = set(tagsL)

            photos.append(Photo(n, O, nT, tagsS, tagsL))
            n+=1

    return N, photos