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

    primes = []
    counter = 0
    # while counter < 11:
    for i in range(11, 1000000):
        satisfies = False
        j = 0
        if isPrime(i) == True:
            satisfies = True
            while j < len(str(i)) - 1:
                leftTrunc = str(i)[j + 1:]
                if isPrime(int(leftTrunc)) == False:
                    satisfies = False
                    break
                rightTrunc = str(i)[:len(str(i)) - j - 1]
                if isPrime(int(rightTrunc)) == False:
                    satisfies = False
                    break
                print(rightTrunc)
                j += 1
        if satisfies == True:
            #      counter += 1
            primes.append(i)

    print(sum(primes))


if __name__ == '__main__':
    main()
