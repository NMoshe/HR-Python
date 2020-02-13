if __name__ == '__main__':
    num = int(input())
    n = set(map(int, input().split()))
    num2 = int(input())
    m = set(map(int, input().split()))
    ans = list(map(int, n.difference(m)))
    ans.extend(m.difference(n))
    print('\n'.join(map(str, sorted(ans))))
