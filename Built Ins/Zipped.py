if __name__ == '__main__':
    n, x = map(int, input().split())
    listA = []
    for i in range(x):
        inp = list(map(float, input().split()))
        listA.append(inp)

    for x in list(zip(*listA)):
        print(sum(x) / len(x))

