from itertools import groupby

if __name__ == '__main__':
    inputA = input()
    for i, k in groupby(inputA):
        print(f'({len(list(k))}, {int(i)})', end=' ')
