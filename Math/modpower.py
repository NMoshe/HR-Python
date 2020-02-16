if __name__ == '__main__':
    #numA = int(input())
    #numB = int(input())
    #numC = int(input())
    numA, numB, numC = [int(input()) for _ in range(3)]
    print(pow(numA, numB), pow(numA, numB, numC), sep='\n')
