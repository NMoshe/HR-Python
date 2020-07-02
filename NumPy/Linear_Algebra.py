import numpy
numpy.set_printoptions(legacy='1.13')

if __name__ == '__main__':
    irr = int(input())
    arr1 = []
    for x in range(irr):
        arr2 = list(map(float, input().split()))
        arr1.append(arr2)

    print(f"{numpy.linalg.det(arr1):0.2f}")