# year = int(input())


def is_leap(x):
    if x % 100 == 0:
        if x % 400 == 0:
            return True
        else:
            return False
    elif x % 4 == 0:
        return True
    else:
        return False
