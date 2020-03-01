import xml.etree.ElementTree as etree


def get_attr_number(node):
    ans = [len(elem.items()) for elem in node.iter()]
    return sum(ans)


if __name__ == '__main__':
    xml1 = []
    for x in range(int(input())):
        xml1.append(input())
    tree = etree.ElementTree(etree.fromstring('\n'.join(xml1)))
    print(get_attr_number(tree))
