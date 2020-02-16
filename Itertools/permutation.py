from itertools import permutations

if __name__ == '__main__':
    inputA = input().split()
    gener = permutations(sorted(inputA[0]), int(inputA[1]))
    for x in gener:
        print(''.join(x))
