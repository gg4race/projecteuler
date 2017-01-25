def main():

    #find 10001st prime

    def isPrime(num, factors):
        isPrime = True
        #check if is prime by dividing by primes smaller than itself
        for factor in factors:
            if num % factor == 0:
                isPrime = False
                break
        return isPrime


    primes = [2]
    j = 2

    while len(primes) <= 10001:
        if (isPrime(j, primes)):
            primes.append(j)
        j += 1

    print(primes[-1])


if __name__ == '__main__':
    main()
