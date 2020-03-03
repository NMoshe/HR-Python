import numpy

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    arr1 = numpy.array([input().strip().split() for x in range(n)], int)
    print(numpy.max(numpy.min(arr1, axis=1)))