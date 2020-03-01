import re

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []
matrixS = ''
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
matrix = list(zip(*matrix))
for x in matrix:
    for i in x:
        matrixS += i
ans = re.sub(r'(?<=\w)(\W)+(?=\w)', ' ', matrixS)
print(ans)
