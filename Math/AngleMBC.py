import math

if __name__ == '__main__':
    numA = int(input())
    numB = int(input())

    ans = math.atan2(numA, numB)
    print(str(round(ans * 180 / math.pi)) + '°')
