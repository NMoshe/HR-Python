if __name__ == '__main__':
    palindromes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99]
    n = int(input())
    listN = [int(x) for x in input().split()]
    if all(0 < x < 100 for x in listN):
        if any(x in palindromes for x in listN):
            print(True)
        else:
            print(False)
    else:
        print(False)



