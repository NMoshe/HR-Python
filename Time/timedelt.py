import datetime


def time_delta(t1, t2):
    time1 = datetime.datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    time2 = datetime.datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    ans = (time1 - time2).total_seconds()
    print(f'{abs(ans):.0f}')


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        t1 = input()
        t2 = input()
        time_delta(t1, t2)
