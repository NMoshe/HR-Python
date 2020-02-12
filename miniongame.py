import re


def minion_game(stringname):
    Stuart = 0
    Kevin = 0
    for i in range(len(stringname)):
        if stringname[i] in 'AEOIU':
            Kevin += (len(stringname) - i)
        else:
            Stuart += (len(stringname) - i)
    # for j in range(i, length):
    #   cut = stringname[i:j + 1]
    #   if cut[0] in 'AEOIU':
    #      Kevin += 1
    #  else:
    #      Stuart += 1

    # [stringname[i:j + 1] for i in range(length) for j in range(i, length)]
    # for i in subs:
    # if i[0][0] in 'AEOIU':
    #  Kevinl.append(i)
    # else:
    #  Stuartl.append(i)

    if Stuart > Kevin:
        print(f'Stuart {Stuart}')
    elif Kevin > Stuart:
        print(f'Kevin {Kevin}')
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)
