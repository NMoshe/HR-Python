import re

if __name__ == '__main__':
    uidRegex = re.compile(r'^(?!.*(.).*\1)'
                          r'(?=(?:.*[A-Z]){2,})'
                          r'(?=(?:.*\d){3,})'
                          r'([a-zA-Z0-9]){10}$')
    for x in range(int(input())):
        if re.match(uidRegex, input()):
            print('Valid')
        else:
            print('Invalid')
