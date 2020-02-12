if __name__ == '__main__':
    n = int(input())
    l = []

    for x in range(n):
        nInput = input().split()
        if len(nInput) == 1:
            command = nInput[0]
        if len(nInput) == 2:
            command = nInput[0]
            e = int(nInput[1])
        if len(nInput) == 3:
            command = nInput[0]
            i = int(nInput[1])
            e = int(nInput[2])

        if 'insert' in nInput:
            l.insert(i, e)
        elif 'print' in nInput:
            print(l)
        elif 'remove' in nInput:
            l.remove(e)
        elif 'append' in nInput:
            l.append(e)
        elif 'sort' in nInput:
            l.sort()
        elif 'pop' in nInput:
            if not l:
                continue
            l.pop()
        elif 'reverse' in nInput:
            l.reverse()
