if __name__ == '__main__':
    num = int(input())
    ans = set()
    # for i in range(1, num + 1):
    #    ans.add(str(input()))
    # print(len(ans))
    print(len(set([(str(input())) for x in range(1, num + 1)])))
