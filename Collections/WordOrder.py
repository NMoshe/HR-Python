from collections import OrderedDict

if __name__ == '__main__':
    num = int(input())
    item = OrderedDict()
    count = 1
    for x in range(num):
        ran = input()
        if item.get(ran):
            item[ran] += count
        else:
            item[ran] = count
    print(len(item))
    for v in item.values():
        print(v, end=' ')
