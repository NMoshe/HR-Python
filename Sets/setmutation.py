if __name__ == '__main__':
    num = int(input())
    numSet = set(map(int, input().split()))
    numC = int(input())

    for x in range(numC):
        nInput = input().split()
        nInput2 = input().split()

        if 'intersection_update' in nInput:
            numSet.intersection_update(nInput2)
            print(numSet)
        elif 'update' in nInput:
            numSet.update(nInput2)
            print(numSet)
        elif 'symmetric_difference_update' in nInput:
            numSet.symmetric_difference_update(nInput2)
            print(numSet)
        elif 'difference_update' in nInput:
            numSet.difference_update(nInput2)
            print(numSet)
    print(sum(map(int, numSet)))
