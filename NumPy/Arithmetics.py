import numpy


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    arr1 = numpy.array([input().strip().split() for x in range(n)], int)
    arr2 = numpy.array([input().strip().split() for x in range(n)], int)

    print(numpy.add(arr1, arr2), numpy.subtract(arr1, arr2), numpy.multiply(arr1, arr2),
          arr1 // arr2, numpy.mod(arr1, arr2), numpy.power(arr1, arr2), sep='\n')
