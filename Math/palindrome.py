for i in range(1, int(input()) + 1):
    print(*(range(1, i)), len(range(i)), *(range(i - 1, 0, -1)))
    #print(((10 ** i - 1) // 9) ** 2)
