def main():
    dig = 0
    prod = 1
    digFound = [False] * 7
    for i in range(1, 1000001):
        dig = dig + len(str(i))

        if digFound[1] == False:
            if dig > 9:
                prod *= int(str(i)[len(str(i)) - (dig - 9)])
                digFound[1] = True

        if digFound[2] == False:
            if dig > 99:
                prod *= int(str(i)[len(str(i)) - (dig - 99)])
                print(str(i)[len(str(i)) - (dig - 99)])
                digFound[2] = True

        if digFound[3] == False:
            if dig > 999:
                prod *= int(str(i)[len(str(i)) - (dig - 999)])
                print(str(i)[len(str(i)) - (dig - 999)])
                digFound[3] = True

        if digFound[4] == False:
            if dig > 9999:
                prod *= int(str(i)[len(str(i)) - (dig - 9999)])
                print(str(i)[len(str(i)) - (dig - 9999)])
                digFound[4] = True

        if digFound[5] == False:
            if dig > 99999:
                prod *= int(str(i)[len(str(i)) - (dig - 99999)])
                print(str(i)[len(str(i)) - (dig - 99999)])
                digFound[5] = True

        if digFound[6] == False:
            if dig > 999999:
                prod *= int(str(i)[len(str(i)) - (dig - 999999)])
                print(str(i)[len(str(i)) - (dig - 999999)])
                digFound[6] = True

    print(prod)


if __name__ == '__main__':
    main()
