from collections import deque

if __name__ == '__main__':
    n = int(input())
    d = deque()
    for x in range(n):
        command = input().split()

        if 'append' in command:
            d.append(command[1])
        elif 'appendleft' in command:
            d.appendleft(command[1])
        elif 'pop' in command:
            if not d:
                continue
            else:
                d.pop()
        elif 'popleft' in command:
            if not d:
                continue
            else:
                d.popleft()
    for x in d:
        print(x, end='\n')