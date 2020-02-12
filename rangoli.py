import string


def print_rangoli(size):
    al = string.ascii_lowercase[0:size]
    print(al)
    for i in range(size - 1, -size, -1):
        #x = abs(i)
        line = al[size:i:-1] + al[i:size]
        print('--' * i + '-'.join(line) + '--' * i)


# your code goes here

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
