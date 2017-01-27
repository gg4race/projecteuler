def main():
    import math

    def findNumberOfFactors(num):
        factors = 2
        for i in range(2, int(num ** 0.5)):
            if num % i == 0:
                factors += 2

        if not (math.sqrt(num) - int(math.sqrt(num))):
            factors += 1
        return factors

    found = False
    currSum = 1
    currInt = 2

    while not found:
        if findNumberOfFactors(currSum + currInt) > 500:
            found = True
            print (currSum + currInt)
        currSum += currInt
        currInt += 1


if __name__ == '__main__':
    main()
