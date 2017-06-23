def main():
    currnum = 1
    toAdd = 2
    sum1 = 1
    cyclecount = 1
    elementcount = 1
    while elementcount < 1001:
        cyclecount += 1
        elementcount += 2

    print(cyclecount)

    for sides in range(cyclecount - 1):
        for vertices in range(4):
            currnum += toAdd
            sum1 += currnum
        toAdd += 2

    print(sum1)


if __name__ == '__main__':
    main()
