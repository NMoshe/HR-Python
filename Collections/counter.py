from collections import Counter

if __name__ == '__main__':
    nShoes = int(input())
    sShoes = Counter(map(int, input().split()))
    customer = int(input())
    cost = 0

    for x in range(customer):
        cust = list(map(int, input().split()))
        if cust[0] in sShoes.keys():
            sShoes[cust[0]] -= 1
            if sShoes[cust[0]] == 0:
                del sShoes[cust[0]]
            cost += cust[1]
        else:
            continue

    print(cost)
