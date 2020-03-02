import numpy


def alter(l):
    cShape = numpy.array(l)
    cShape.shape = (3, 3)
    return cShape


arr = list(map(int, input().split()))

print(alter(arr))
