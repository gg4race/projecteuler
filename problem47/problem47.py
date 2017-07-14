def main():
    def primes(n):
        factors = set()
        d = 2
        while d * d <= n:
            while (n % d) == 0:
                factors.add(d)
                n /= d
            d += 1
        if n > 1:
            factors.add(n)
        return factors

    found = False
    curr = 2

    while not found:
        primes1 = primes(curr)
        if len(primes1) == 4:
            primes2 = primes(curr + 1)
            if len(primes2) == 4:
                primes3 = primes(curr + 2)
                if len(primes3) == 4:
                    primes4 = primes(curr + 3)
                    if len(primes4) == 4:
                        found = True
                        print(curr)
        curr += 1


if __name__ == '__main__':
    main()
