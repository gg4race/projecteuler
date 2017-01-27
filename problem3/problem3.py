def main():
    i = 2
    n = 600851475143

    while (n > 1 and i * i <= n):   #i * i limit makes code more efficient
        while n % i == 0:
            n /= i
        i += 1

    print max((i-1), n)


if __name__ == '__main__':
    main()
