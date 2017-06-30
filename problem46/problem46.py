def main():
    def isPrime(n):
        if n < 2: return "Neither prime, nor composite"
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = []

    # returns the nth prime number
    def nthPrime(n):
        numberOfPrimes = 0
        prime = 1

        while numberOfPrimes < n:
            prime += 1
            if isPrime(prime):
                numberOfPrimes += 1
                primes.append(prime)
        return prime

    nthPrime(10000)

    for i in range(3, 10000, 2):
        if i not in primes:
            found = False
            currPrime = 2
            j = 0
            while currPrime <= i:
                leftover = int(((i - currPrime) / 2) ** 0.5)
                if leftover ** 2 * 2 + currPrime == i:
                    found = True
                j += 1
                currPrime = primes[j]
            if found == False:
                print("not found: ", i)

    print(maxSum, maxCount, j - 1)


if __name__ == '__main__':
    main()
