def weird(n):
    if n % 2 == 0:
        if 2 <= n <= 5:
            print('Not Weird')
        elif 6 <= n <= 20:
            print('Weird')
        elif n >= 20:
            print('not Weird')
    else:
        print('Weird')


if __name__ == '__main__':
    weird(4)
    weird(13)
    weird(22)
