def wrapper(f):
    def fun(l):
        # f(["+91 "+c[-10:-5]+" "+c[-5:] for c in l])
        listA = []
        for i in l:
            if i[0:2] == '91' and len(i) == 12:
                i = '+' + i[0:2] + ' ' + i[2:7] + ' ' + i[7:]
                listA.append(i)
            elif i[0:3] == '+91':
                i = '+91' + ' ' + i[3:8] + ' ' + i[8:]
                listA.append(i)
            elif len(i) == 10:
                i = '+91' + ' ' + i[0:5] + ' ' + i[5:]
                listA.append(i)
            elif len(i) == 11:
                i = '+91' + ' ' + i[1:6] + ' ' + i[6:]
                listA.append(i)
        return f(listA)
    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
