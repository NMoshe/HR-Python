def runnerup(y):
    c = sorted(list(dict.fromkeys(y)))
    return print(c[-2])


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    runnerup(arr)
