#!/bin/python3


import os


#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    depth = valley = 0
    for step in path:
        if step == 'U':
            depth += 1
            if depth == 0:
                valley += 1
        else:
            depth -= 1
    print(valley)


if __name__ == '__main__':
    steps = int(input().strip())
    path = input()
    result = countingValleys(steps, path)
