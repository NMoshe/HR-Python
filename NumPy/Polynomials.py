import numpy

if __name__ == '__main__':
    arr1 = list(map(float, input().split()))
    point_x = int(input())
    
    print(numpy.polyval(arr1, point_x))