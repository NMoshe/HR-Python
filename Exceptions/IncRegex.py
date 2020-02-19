import re

if __name__ == '__main__':
    t = int(input())
    for x in range(t):
        try:
            a = input()
            re.compile(a)
            print(True)
        except Exception:
            print(False)
