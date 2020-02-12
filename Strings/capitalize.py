#!/bin/python3

import os


# Complete the solve function below.
def solve(s):
    # x, y = s.split(" ")
    # if x[0].islower:
    # c = x[0].upper() + x[1:]
    # else:
    # c = x
    # if y[0].islower():
    # z = y[0].upper() + y[1:]
    # else:
    # z = y
    # s = c + ' ' + z
    # print(s)
    return ' '.join(map(str.capitalize, s.split(' ')))


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # s = input()
    # result = solve(s)
    # fptr.write(result + '\n')
    # fptr.close()
    print(solve('1wqam hwehth'))
