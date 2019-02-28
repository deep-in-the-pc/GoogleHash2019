from utility19 import *

n, photos = readInputB("c_memorable_moments")


photos.sort(key=lambda x: x.nTags)



slide = list()

PhotosV = []
PhotosH = []

for pho in photos:
    if(pho.Orientation == 'V'):
        PhotosV.append(pho)
    else:
        PhotosH.append(pho)

PhotosV.sort(key=lambda x: -x.nTags)

for pho1 in PhotosV:
    for pho2 in PhotosV:
        pho1.merge

print(PhotosV[0])

