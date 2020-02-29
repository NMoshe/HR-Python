if __name__ == '__main__':
    '''listA = []
    for i in range(int(input())):
        listA.append(input())
    s = ('\n'.join(listA))
    s = s.replace(' && ', ' and ')
    s = s.replace(' || ', ' or ')
    print(s)'''

    for _ in range(int(input())):
        line = input()
        while ' && ' in line or ' || ' in line:
            line = line.replace(" && ", " and ").replace(" || ", " or ")
        print(line)
