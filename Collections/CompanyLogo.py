if __name__ == '__main__':
    logo = input()
    company = dict()
    count = 1
    #count2 = 0
    for x in logo:
        if company.get(x):
            company[x] += count
        else:
            company[x] = count
    company2 = sorted(company, key=lambda k: (-company[k], k))
    for k in company2[:3]:
        #count2 += 1
        #if count2 > 3:
         #   break
        #else:
        print(k, company[k])

'''from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    pass
[print(*c) for c in OrderedCounter(sorted(input())).most_common(3)]'''