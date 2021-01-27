#!/bin/python3


# Complete the hourglassSum function below.
def hourglassSum(arr):
    hourglassList = []
    for x in range(len(arr) - 2):
        for j in range(len(arr) - 2):
            hourglassList.append(arr[x][j] + arr[x][j + 1] + arr[x][j + 2] + arr[x + 1][j + 1] +
                       arr[x + 2][j] + arr[x + 2][j + 1] + arr[x + 2][j + 2])
            """print(arr[x][j])"""

    print(max(hourglassList))


if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    result = hourglassSum(arr)
