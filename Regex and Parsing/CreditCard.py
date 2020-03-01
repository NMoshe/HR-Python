import re
'''    creditRegex = re.compile(r'(?!.*(?:\d)\\1{3,})'
                          r'(?!(?:\s\,\_))'
                          r'^([456]{1}[0-9]{15})$'
                          r'|^(?:[456]{1}\d{3}\-?){1}(?:\d{4}\-?){2}\d{4}$')'''

if __name__ == '__main__':
    creditRegex = re.compile(r'^(?!.*(\d)(-?\1){3})'
                             r'[456]\d{3}(?:-?\d{4}){3}$')
    for x in range(int(input())):
        if re.match(creditRegex, input()):
            print('Valid')
        else:
            print('Invalid')
