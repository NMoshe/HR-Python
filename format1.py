def print_formatted(number):
    test = len(f'{number:b}')
    for x in range(1, number + 1):
        print(f'{x:{test}} {x:{test}o} {x:{test}X} {x:{test}b}')


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
