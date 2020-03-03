import numpy

numpy.set_printoptions(legacy='1.13')

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    arr1 = numpy.array([input().strip().split() for x in range(n)], int)
    print(numpy.mean(arr1, axis=1), numpy.var(arr1, axis=0), numpy.std(arr1, axis=None), sep='\n')
