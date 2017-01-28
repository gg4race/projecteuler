def main():
    def findFactors(n):
        i = 2
        factors = [1]
        while i * i <= n:
            if n % i == 0:
                factors.append(i)
                if int(i * i) != n:
                    factors.append(int(n / i))
            i += 1

        return factors

    amicables = set()
    for j in range(2, 10000):
        sum1 = sum(findFactors(j))
        sum2 = sum(findFactors(sum1))
        if sum2 == j and sum2 != sum1:
            amicables.add(j)
            if sum1 < 10000:
                amicables.add(sum1)

    print(sum(list(amicables)))


if __name__ == '__main__':
    main()
