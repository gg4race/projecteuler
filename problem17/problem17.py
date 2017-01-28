def main():
    # add 1-9, 10-19, 20-99 in sections
    len_1to9 = 19 + 3 + 5 + 5 + 4
    len_10to19 = 3 + 6 + 6 + 8 + 8 + 7 + 7 + 9 + 8 + 8
    len_20 = 6
    len_30 = 6
    len_40 = 5
    len_50 = 5
    len_60 = 5
    len_70 = 7
    len_80 = 6
    len_90 = 6
    len_hundred = 7
    len_and = 3

    # sum 20-99
    len_20to99 = (len_20 + len_30 + len_40 + len_50 + len_60 + len_70 + len_80 + len_90) * 10 + len_1to9 * 8

    # sum 1-99
    len_1to99 = len_1to9 + len_10to19 + len_20to99

    # total
    len_total = len_1to99 + len_1to9 * 100 + len_hundred * (99 * 9 + 9) + len_and * 99 * 9 + len_1to99 * 9 + 11

    print(len_total)


if __name__ == '__main__':
    main()
