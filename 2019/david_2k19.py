from utility19 import *

n, photos = readInput("a_example")


photos.sort(key=lambda x: x.nTags)

for i in photos:
    print(i.id, i.nTags, i.tags, i.Orientation)

slide = list()

while(len(photos)>0):
    for i in range(len(photos)):
        for n in range(len(photos[i:])):
            for tag in photos[i].tagsL:
                if tag in photos[n].tagsS:
                    slide.append(photos.pop(n))


for i in slide:
    print(i.id, i.nTags, i.tags, i.Orientation)

