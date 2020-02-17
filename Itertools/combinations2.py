from itertools import combinations_with_replacement

if __name__ == '__main__':
    inputA = input().split()
    gener = combinations_with_replacement(sorted(inputA[0]), int(inputA[1]))
    for x in gener:
        print(''.join(x))