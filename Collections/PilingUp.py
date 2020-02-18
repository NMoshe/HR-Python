from collections import deque

if __name__ == '__main__':
    for x in range(int(input())):
        int(input())
        cube = deque(map(int, input().split()))
        if max(cube) not in (cube[0], cube[-1]):
            print('No')
        else:
            print('Yes')