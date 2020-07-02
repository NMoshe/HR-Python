import numpy

if __name__ == '__main__':
    arr1 = numpy.array([input().split()], int)
    arr2 = numpy.array([input().split()], int)

    print(int(numpy.inner(arr1, arr2)))
    print(numpy.outer(arr1, arr2))