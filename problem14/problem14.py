def main():
    maxLength = 0
    maxInt = 0

    for i in range(2, 1000000):
        currLength = 0
        n = i
        while n > 1:
            if n % 2 == 0:
                n /= 2
            else:
                n = 3 * n + 1
            currLength += 1
        if currLength > maxLength:
            maxLength = currLength
            maxInt = i

    print(maxInt)


if __name__ == '__main__':
    main()
