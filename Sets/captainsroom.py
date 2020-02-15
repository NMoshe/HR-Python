if __name__ == '__main__':
    num = int(input())
    n = list(map(int, input().split()))
    '''ans = dict()
    for x in n:
        ans[x] = n.count(x)
    for k, v in ans.items():
        if v == 1:
            print(k)'''
    # myset = set(n)
    # print(((sum(myset)*num)-(sum(n)))//(num-1))
    myset2 = set()
    myset3 = set()

    for x in n:
        if x in myset2:
            myset3.add(x)
        else:
            myset2.add(x)
    ans = list(myset2.difference(myset3))
    print(ans[0])
