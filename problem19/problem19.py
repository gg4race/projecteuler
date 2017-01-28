def main():
    days1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days2 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    totalDays = 0
    for year in range(1901, 2001):
        if year % 100 == 0:
            if year % 400 == 0:
                totalDays += sum(days2)
            else:
                totalDays += sum(days1)
        else:
            if year % 4 == 0:
                totalDays += sum(days2)
            else:
                totalDays += sum(days1)

    print(totalDays)


if __name__ == '__main__':
    main()
