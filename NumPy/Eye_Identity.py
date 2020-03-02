import numpy
numpy.set_printoptions(legacy='1.13')

if __name__ == '__main__':
    a, b = list(map(int, input().split()))

    print(numpy.eye(a, b, k=0))