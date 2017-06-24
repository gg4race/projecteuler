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

    currMax = 0
    tempMax = 0

    maxI = 0
    maxJ = 0
    dict = dict()

    for i in range(-1000, 1001):
        for j in range(-1000, 1001):
            loopPrime = True
            currN = 0
            while loopPrime:
                prod = currN * currN + i * currN + j
                if isPrime(prod) == False:
                    loopPrime = False
                    if currN >= tempMax:
                        tempMax = currN
                        maxI = i
                        maxJ = j
                currN = currN + 1

    print(str(tempMax) + ', ' + str(maxI) + ', ' + str(maxJ) + ', ' + str(maxI * maxJ))


if __name__ == '__main__':
    main()
