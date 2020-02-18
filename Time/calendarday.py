import calendar

if __name__ == '__main__':
    day = list(map(int, input().split()))
    ans = calendar.weekday(day[2], day[0], day[1])
    if ans == 0:
        print('MONDAY')
    elif ans == 1:
        print('TUESDAY')
    elif ans == 2:
        print('WEDNESDAY')
    elif ans == 3:
        print('THURSDAY')
    elif ans == 4:
        print('FRIDAY')
    elif ans == 5:
        print('SATURDAY')
    elif ans == 6:
        print('SUNDAY')
    # print((calendar.day_name[calendar.weekday(day[2], day[0], day[1])]).upper())
