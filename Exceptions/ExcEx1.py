if __name__ == '__main__':
    t = int(input())
    for x in range(t):
        try:
            a, b = list(map(int, input().split()))
            print(a // b)
        except (ZeroDivisionError, ValueError) as e:
            print('Error Code:', e)
