import numpy

if __name__ == '__main__':
    a = list(map(int, input().split()))

    print(numpy.zeros(a, dtype=int))
    print(numpy.ones(a, dtype=int))
