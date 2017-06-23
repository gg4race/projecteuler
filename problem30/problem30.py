def main():
    upper = 6 * (9 ** 5)
    print(upper)
    res = 0

    powers = [0] * 10
    for i in range(10):
        powers[i] = i ** 5

    print(powers)

    for j in range(upper + 1):
        digits = [int(x) for x in str(j)]
        tempSum = 0
        for digit in digits:
            tempSum += powers[digit]

        if tempSum == j:
            res += tempSum

    print(res - 1)


if __name__ == '__main__':
    main()
