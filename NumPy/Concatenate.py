import numpy

if __name__ == '__main__':
    n, m, p = list(map(int, input().split()))
    listA =[]

    for x in range(n + m):
        user = list(map(int, input().split()))
        listA.append(user)

    ans = numpy.array(listA)
    print(ans)