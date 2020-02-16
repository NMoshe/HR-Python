from itertools import product

if __name__ == '__main__':
    listA = map(int, input().split())
    listB = map(int, input().split())

    print(*product(listA, listB))
