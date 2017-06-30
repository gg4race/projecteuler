def main():
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

    maxCount = 0
    maxSum = 0
    currSum = 0
    lastPrime = 0
    for i in range(2, 99):
        print(i)
        if isPrime(i):
            currSum = i
            j = i + 1
            c = 1
            while currSum <= 1000000:
                if isPrime(j):
                    lastPrime = j
                    currSum += j
                    if currSum <= 1000000:
                        c += 1
                        if isPrime(currSum):
                            if c >= maxCount:
                                maxCount = c
                                maxSum = currSum
                j += 1

    print(maxSum, maxCount, j - 1)


if __name__ == '__main__':
    main()
