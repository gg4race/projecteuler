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

    def rotateString(in_arr):
        temp = in_arr[len(in_arr) - 1]
        new_arr = []
        new_arr.append(temp)
        for i in range(0, len(in_arr) - 1):
            new_arr.append(in_arr[i])
        return ''.join(new_arr)

    currCount = 0

    for i in range(2, 1000000):
        satisfies = True
        currString = str(i)
        for rot in range(0, len(str(i))):

            if isPrime(int(currString)) == False:
                satisfies = False
                break;
            rotated = str(rotateString(currString))
            currString = rotated
        if satisfies == True:
            print(i)
            currCount += 1

    print(currCount)


if __name__ == '__main__':
    main()
