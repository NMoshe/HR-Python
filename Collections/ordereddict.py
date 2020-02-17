from collections import OrderedDict

if __name__ == '__main__':
    num = int(input())
    item = OrderedDict()

    for x in range(num):
        *name, price = input().split()
        name2 = ' '.join(name)
        if item.get(name2):
            item[name2] += int(price)
        else:
            item[name2] = int(price)

    for k, v in item.items():
        print(k, v)
