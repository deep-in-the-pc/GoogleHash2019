from utility19 import *

n, photos = readInputB("a_example")


photos.sort(key=lambda x: x.nTags)

for i in photos:
    print(i.id, i.nTags, i.tags, i.Orientation)

slide = list()

photosV = []

for pho in photos:
    if(pho.Orien == 'V'):
        photosV.append(pho)

ordPhotosV =  sortPhotos(photosV)

