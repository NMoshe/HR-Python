import numpy


if __name__ == '__main__':
    n = int(input())
    arr1 = numpy.array([input().strip().split() for x in range(n)], int)
    arr2 = numpy.array([input().strip().split() for x in range(n)], int)

    print(numpy.dot(arr1, arr2))