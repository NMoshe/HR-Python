import xml.etree.ElementTree as etree

maxdepth = 0

'''maxdepth = 0
for i in range(int(input())):
    depth = input().count('    ')
    if maxdepth < depth:
        maxdepth = depth
print(maxdepth)'''


def depth(elem, level):
    global maxdepth
    if maxdepth == level:
        maxdepth += 1
    for i in elem:
        depth(i, level + 1)


if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml = xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
