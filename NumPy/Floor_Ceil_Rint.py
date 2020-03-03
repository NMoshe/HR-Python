import numpy
numpy.set_printoptions(legacy='1.13')

if __name__ == '__main__':
    arr = numpy.array(list(map(float, input().split())))
    print(numpy.floor(arr), numpy.ceil(arr), numpy.rint(arr), sep='\n')