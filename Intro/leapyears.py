def leap(year):
    if year % 100 == 0:
        if year % 400 == 0:
            print(year)
        else:
            print(f'{year} is not a leap year')
    elif year % 4 == 0:
        print(year)
    else:
        print(f'{year} is not a leap year')


if __name__ == '__main__':
    leap(1900)
    leap(2000)
    leap(2400)
    leap(2020)
    leap(1990)
    leap(2024)
    leap(2025)
    leap(8)
