def main():
    found = False
    i = 144
    j = 144
    k = 144
    hex = 1
    pent = 1
    tri = 1

    while found == False:
        hex = i * (2 * i - 1)

        while pent <= hex:
            pent = j * (3 * j - 1) / 2
            while tri <= pent:
                tri = k * (k + 1) / 2
                if hex == pent and hex == tri:
                    found = True
                    print(i, hex)
                    break;
                k += 1
            j += 1
        i += 1


if __name__ == '__main__':
    main()
