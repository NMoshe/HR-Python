import numpy

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    listA = []
    for x in range(n):
        user = list(map(int, input().split()))
        listA.append(user)
    ans = numpy.array(listA)
    print(ans.transpose())
    print(ans.flatten())
