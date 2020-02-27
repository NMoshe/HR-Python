if __name__ == '__main__':
    n, m = map(int, input().split())
    listA = []
    for x in range(n):
        listA.append(list(map(int, input().split())))
    k = int(input())
    for x in sorted(listA, key=lambda x: x[k]):
        print(*x)