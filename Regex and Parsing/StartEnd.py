if __name__ == '__main__':
    s, k = input(), input()
    ans = [(i, len(k) + (i - 1)) for i in range(0, len(s)) if s[i:len(k) + i] == k]
    for x in ans:
        print(x)
    if not ans:
        print('(-1, -1)')
