if __name__ == '__main__':
    num = int(input())
    n = set(input().split())
    num2 = int(input())
    m = set(input().split())
    print(len(n.intersection(m)))