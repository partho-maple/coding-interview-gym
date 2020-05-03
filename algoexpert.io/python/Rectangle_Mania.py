"""
				x1,y1

x2,y2
"""


def rectangleMania(coords):
    coordSet = set([(coord[0], coord[1]) for coord in coords])
    rectangleCount = 0
    for i in range(len(coords)):
        for j in range(len(coords)):
            coordOne = coords[i]
            coordTwo = coords[j]
            if coordOne == coordTwo:
                continue
            if (coordOne[0] > coordTwo[0]) and (coordOne[1] > coordTwo[1]):
                if (coordOne[0], coordTwo[1]) in coordSet and (coordTwo[0], coordOne[1]) in coordSet:
                    rectangleCount += 1
    return rectangleCount

