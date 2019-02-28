from utility19 import *
#file = "a_example"
#file = "b_lovely_landscapes"
file = "c_memorable_moments"
n, photos = readInput(file)


photos.sort(key=lambda x: x.nTags)

slides = list()
isPop = 0
lastV = 0
isV = 0
slides.append(photos.pop(0))

while(len(photos)>0):
    print(len(photos))
    if(photos[0].Orientation == 'V'):
        isV=1
    for n in range(len(photos[0:])):
        if (isPop):
            isPop = 0
            break
        if (lastV == 1 and not isV):
            continue
        if(slides[-1].comparePhotos(photos[n])>0):
            if(photos[n].Orientation == 'V'):
                lastV=1
                slides[-1] = slides[-1].mergePhoto(photos.pop(n))
            else:
                lastV=0
                slides.append(photos.pop(n))
            isPop = 1
            break


#for i in slides:
#    print(i.id, i.nTags, i.tagsL, i.Orientation)

exportOutputs(file, slides)