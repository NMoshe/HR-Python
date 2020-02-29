def fibonacci(n):
    if n == 0:
        return []
    if n == 1:
        return [0]
    a, b = 0, 1
    ans = [0, 1]
    for _ in range(0, n - 2):
        a, b = b, a + b
        ans.append(b)
    return ans


if __name__ == '__main__':
    n = int(input())
    print(list(map(lambda x: x ** 3, fibonacci(n))))
