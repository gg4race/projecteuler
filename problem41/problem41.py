def main():
    import itertools
    def isPrime(n):
        '''check if integer n is a prime'''
        # make sure n is a positive integer
        n = abs(int(n))
        # 0 and 1 are not primes
        if n < 2:
            return False
        # 2 is the only even prime number
        if n == 2:
            return True
            # all other even numbers are not primes
        if not n & 1:
            return False
        # range starts with 3 and only needs to go up the squareroot of n
        # for all odd numbers
        for x in range(3, int(n ** 0.5) + 1, 2):
            if n % x == 0:
                return False
        return True

    pandigitals = itertools.permutations('7654321')

    # pandigs = [int(x) for x in pandigitals]
    for pandigital in pandigitals:
        num = ''.join(str(dig) for dig in pandigital)
        if isPrime(int(num)):
            print(num)


if __name__ == '__main__':
    main()
