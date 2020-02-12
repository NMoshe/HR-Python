if __name__ == '__main__':
    n = int(input())
    integer_list = list(map(int, input().split()))

    hashable = tuple()
    for x in integer_list:
        hashable += (x,)

    print(hash(hashable))
