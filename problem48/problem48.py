def main():
    import math
    sum1 = 0

    for i in range(1, 1001):
        sum1 = sum1 + i ** i

    print(str(sum1)[-10:])


if __name__ == '__main__':
    main()
