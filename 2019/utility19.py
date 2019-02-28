#import numpy as np

class Photo():
    def __init__(self, id, o, nT, tagsS, tagsL, id2=-1):
        self.id = (id, id2)
        self.Orientation = o
        self.nTags = nT
        self.tagsS = tagsS
        self.tagsL = tagsL

    def comparePhotos(self,photo2):
        inters = len(self.tagsS & photo2.tagsS)
        photo1_only = self.tagsS - photo2.tagsS
        photo2_only = photo2.tagsS - self.tagsS

        photo1_only = self.nTags - inters
        photo2_only = photo2.nTags - inters

        return min(inters,photo1_only,photo2_only)

    def mergePhoto(self, photo2):
        tagsS = self.tagsS.union(photo2.tagsS)
        tagsL = list(tagsS)
        nTags = len(tagsL)
        Orien = 'H'
        return Photo(self.id[0], Orien, nTags, tagsS, tagsL, photo2.id[0])
    
    def __str__(self):
        return str(self.__dict__)
        
    def getStringId(self):
        if(self.id[1]==-1):
            return str(self.id[0])

        else:
            return str(self.id[0])+" "+str(self.id[1])

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
    return sorted(photos, key=lambda photo: -photo.nTags) 



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
            outfile.write(i.getStringId() + "\n")
            #n+=1
