from collections import defaultdict

if __name__ == '__main__':
    n, m = map(int, input().split())
    d = defaultdict(list)

    for x in range(1, n + 1):
        d[input()].append(x)

    for x in range(m):
        user = input()
        if user in d:
            print(' '.join(map(str, d[user])))
        else:
            print(-1)