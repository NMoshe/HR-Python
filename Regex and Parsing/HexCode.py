import re
if __name__ == '__main__':
    hexRegex = r".(#[0-9A-Fa-f]{6}|#[0-9A-Fa-f]{3})"
    for _ in range(int(input())):
        line = input()
        ans = re.findall(hexRegex, line)
        if ans:
            print('\n'.join(ans))
        else:
            continue
