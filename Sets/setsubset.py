if __name__ == '__main__':
    testcase = int(input())
    for _ in range(testcase + 1):
        numA = input()
        setA = set(map(int, input().split()))
        numB = input()
        setB = set(map(int, input().split()))
        print(setA.issubset(setB))
