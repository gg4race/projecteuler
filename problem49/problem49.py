def main():
    def isPrime(n):
        if n < 2: return "Neither prime, nor composite"
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = []
    for i in range(1000, 10000):
        if isPrime(i):
            primes.append(i)

    for j in range(len(primes) - 4):
        for k in range(j + 1, len(primes)):
            diff = primes[k] - primes[j]
            if primes[k] + diff in primes:

                prime1 = sorted([c for c in str(primes[j])])
                prime2 = sorted([x for x in str(primes[k])])
                prime3 = sorted([x for x in str(primes[k] + diff)])
                if len([i for i, j in zip(prime1, prime2) if i == j]) == 4 and len(
                        [i for i, j in zip(prime1, prime3) if i == j]) == 4:
                    print(primes[j], primes[k], primes[k] + diff)


if __name__ == '__main__':
    main()
