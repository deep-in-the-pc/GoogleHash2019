import numpy as np

class Photo():
    def __init__(self, o, nT, tags):
        self.Orientation = o
        self.nTags = nT
        self.tags = tags



def readInput(inputFile):
    inputPath = "Data Sets\\"+inputFile+".txt"
    with open(inputPath, 'r') as data:
        photos = list()
        firstline = data.readline()
        N = int(firstline)
        for row in data.readlines():
            for i in row.split():
                O, nT, tags = [int(i) for i in row.split()]
            photos.append(Photo(O, nT, tags))

    return N, photos