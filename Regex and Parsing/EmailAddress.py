import re

if __name__ == '__main__':
    emailRegex = re.compile("^[<][a-zA-Z][\w.-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}[>]$")
    for i in range(int(input())):
        name, email = input().split()
        if re.match(emailRegex, email):
            print(name, email)
        else:
            continue
