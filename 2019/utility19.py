#import numpy as np

class Photo():
    def __init__(self, id, o, nT, tagsS, tagsL):
        self.id = id
        self.Orientation = o
        self.nTags = nT
        self.tagsS = tagsS
        self.tagsL = tagsL

    def comparePhotos(self,photo2):
        inters = self.tags & photo2.tags
        photo1_only = self.tags - photo2.tags
        photo2_only = photo2.tags - self.tags

        photo1_only = self.nT - inters
        photo2_only = photo2.nT - inters

        return min(inters,photo1_only,photo2_only)

    def mergePhoto(self, photo2):
        tagsS = self.tagsS.union(photo2.tagsS)
        tagsL = list(tagsS)
        nTags = len(tagsL)
        Orien = 'H'
        return Photo((self.id,photo2.id), Orien, nTags, tagsS, tagsL)
    


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



def readInputB(inputFile):
    inputPath = "C:\\Users\\Bruno Reis\\Desktop\\google hash\\GoogleHash2019\\2019\\Data Sets\\"+inputFile+".txt"
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

def exportOutputs(outputFile, Outputs):
    outputPath = "Data Sets\\" + outputFile + ".out"
    with open(outputPath, 'w') as outfile:
        #n = 1
        outfile.write(str(len(Outputs))+"\n")
        for i in Outputs:
            outfile.write(str(i.id)+"\n")
            #n+=1


def sortPhotos(photos):
    sorted(photos, key=lambda photo: photo.n) 