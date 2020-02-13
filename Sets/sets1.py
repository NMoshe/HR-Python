def average(array):
    sete = set(array)
    return sum(sete) / len(sete)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
