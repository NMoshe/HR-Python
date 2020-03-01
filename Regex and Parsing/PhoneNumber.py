import re

if __name__ == '__main__':
    regex_pattern = r'^[7-9]([0-9]{9})$'
    for i in range(int(input())):
        if re.match(regex_pattern, input()):
            print('YES')
        else:
            print('NO')