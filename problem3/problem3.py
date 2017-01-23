def main():
    i = 2
    n = 600851475143

    while (i * i <= n):
        while (n > 1):
            while n % i == 0:
                n /= i
            i += 1

    print (i-1)


if __name__ == '__main__':
    main()
