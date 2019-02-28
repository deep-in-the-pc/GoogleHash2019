import numpy as np

class Photo():
    def __init__(self, o, nT, tags):
        self.Orientation = o
        self.nTags = nT
        self.tags = tags

    def comparePhotos(self,photo2):
        inters
        photo1_only
        photo2_only
        for tag in self.tags:
            for tag_2 in self.photo2:
                if tag == tag_2:
                    inters += 1

        photo1_only = self.nT - inters
        photo2_only = photo2.nT - inters

        return min(inters,photo1_only,photo2_only)


def readInput(inputFile):
    inputPath = "Data Sets\\"+inputFile+".txt"
    with open(inputPath, 'r') as data:
        photos = list()
        firstline = data.readline()
        N = int(firstline)
        for row in data.readlines():
            line = row.split()
            O = line[0]
            nT = int(line[1])
            tags = [i for i in line[2:]]

            photos.append(Photo(O, nT, tags))

    return N, photos

def sortPhotos(photos):
    sorted(photos, key=lambda photo: photo.n) 