from itertools import combinations

if __name__ == '__main__':
    inputA = input().split()
    for x in range(1, int(inputA[1]) + 1):
        for i in combinations(sorted(inputA[0]), x):
            print(''.join(i))