#!/bin/python3

# Complete the repeatedString function below.
def repeatedString(s, n):
    c = s.count("a")
    repeated = n // len(s)
    remainder = s[:n % len(s)].count("a")
    return print(c * repeated + remainder)


if __name__ == '__main__':
    s = input()
    n = int(input())
    result = repeatedString(s, n)
