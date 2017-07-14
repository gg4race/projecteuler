def main():
    def isPrime(n):
        if n < 2: return "Neither prime, nor composite"
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    currnum = 1
    toAdd = 2
    '''sum1 = 1
    cyclecount = 1
    elementcount = 1
    while elementcount < 1001:
      cyclecount+=1
      elementcount +=2'''

    primes = []
    nonprimes = []
    for sides in range(20000):
        for vertices in range(4):
            currnum += toAdd
            if isPrime(currnum):
                primes.append(currnum)
            else:
                nonprimes.append(currnum)
            if len(primes) / (len(nonprimes) + len(primes)) < 0.1:
                print(toAdd)
        # sum1+=currnum
        toAdd += 2

        # print(sum1)


if __name__ == '__main__':
    main()
