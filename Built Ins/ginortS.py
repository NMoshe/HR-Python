if __name__ == '__main__':
    n = list(input())

    x = [x for x in n if x.isdigit()]
    z = [x for x in n if not (x.isdigit() or x[0] == '-' and x[1:].isdigit())]

    z = sorted(z, key=lambda x: (not x.islower(), x))
    x = sorted(x, key=lambda x: (-(int(x) % 2), x))

    for i in x:
        z.append(i)

    for i in z:
        print(i, end='')

    #order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468'
    #print(*sorted(input(), key=order.index), sep='')
