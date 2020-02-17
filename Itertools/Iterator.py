import itertools

if __name__ == '__main__':
    lenA = int(input())
    listA = input().split()
    indiceA = int(input())
    count = 0
    ans = []
    for x in itertools.combinations(listA, indiceA):
        if 'a' in x:
            count += 1
        ans.append(x)

    print(f'{count / len(ans):.4f}')
