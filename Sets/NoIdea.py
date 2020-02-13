def happiness(array, x, y):
    happy = 0
    for i in range(len(array)):
        if array[i] in x:
            happy += 1
        elif array[i] in y:
            happy -= 1
    print(happy)


if __name__ == '__main__':
    na, ma = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    n = set(map(int, input().split()))
    m = set(map(int, input().split()))
    happiness(arr, n, m)
