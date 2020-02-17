from itertools import product

if __name__ == '__main__':
    K, M = map(int, input().split())
    print(M)
    listA = []
    listMax = []
    for x in range(K):
        listA.append(list(map(int, input().split()[1:])))
    #for x in product(*listA):
    listPow = (map(lambda x: sum(i ** 2 for i in x), product(*listA)))
    print(type(listPow))
    print(max(listPow))
