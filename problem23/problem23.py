def main():
    # find abundant numbers
    abds = []
    for i in range(12, 28121):
        j = 2
        divs = [1]
        while j * j <= i:
            if i % j == 0:
                divs.append(j)
                if j != i / j:
                    divs.append(int(i / j))
            j += 1
        currsum = sum(int(d) for d in divs)
        if currsum > i:
            abds.append(i)

    # loop to find find sums of abundant numbers

    sums = set()

    for abd1 in abds:
        for abd2 in abds:
            if abd1 + abd2 <= 28123:
                sums.add(abd1 + abd2)
            else:
                break

    not_sums = []

    for i in range(1, 28124):
        if i not in sums:
            not_sums.append(i)

    print(sum(int(x) for x in not_sums))


if __name__ == '__main__':
    main()
