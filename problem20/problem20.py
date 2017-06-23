def main():
    product = 1

    n = 100

    while n > 0:
        product *= n
        n -= 1

    print(sum(map(int, str(product))))


if __name__ == '__main__':
    main()
