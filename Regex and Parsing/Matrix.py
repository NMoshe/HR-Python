import re

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []
matrixS = ''

for _ in range(n):
    matrix.append(input())

for x in list(zip(*matrix)):
    for i in x:
        matrixS += i

ans = re.sub(r'(?<=\w)(\W)+(?=\w)', ' ', matrixS)
print(ans)
