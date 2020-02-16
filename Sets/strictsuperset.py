if __name__ == '__main__':
    setA = set(map(int, input().split()))
    nSet = int(input())
    numL = []
    ans = True
    '''
    for x in range(nSet):
        numL.extend(input().split())
    print(setA.issuperset(numL))'''
    for x in range(nSet):
        setI = set(map(int, input().split()))
        numL.append(setI)

    for i in numL:
        if not setA.issuperset(i):
            ans = False

    print(ans)