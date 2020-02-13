if __name__ == '__main__':
    num = int(input())
    numSet = set(map(int, input().split()))
    numC = int(input())

    for x in range(numC):
        nInput = input().split()
        if len(nInput) == 1:
            command = nInput[0]
        if len(nInput) == 2:
            command = nInput[0]
            e = int(nInput[1])

        if 'remove' in nInput:
            numSet.remove(e)
        elif 'discard' in nInput:
            numSet.discard(e)
        elif 'pop' in nInput:
            if not numSet:
                continue
            numSet.pop()
    print(sum(numSet))
