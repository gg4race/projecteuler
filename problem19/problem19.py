def main():
    counter = 0
    sundays = 0

    def findTotalDays(year, month):
        if month == 2:
            if year % 100 == 0:
                if year % 400 == 0:
                    return 29
                else:
                    return 28
            else:
                if year % 4 == 0:
                    return 29
                else:
                    return 28
        elif month in (1, 3, 5, 7, 8, 10, 12):
            return 31
        elif month in (4, 6, 9, 11):
            return 30

    for year in range(1901, 2001):
        for month in range(1, 13):
            totalDays = findTotalDays(year, month)
            for day in range(1, totalDays + 1):
                if day == 1:
                    if counter % 7 == 0:
                        sundays += 1
                counter += 1

    print(sundays)


if __name__ == '__main__':
    main()
