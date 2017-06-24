def main():
    from operator import mul
    import functools
    fact = [1]

    for i in range(1, 10):
        fact.append(functools.reduce(mul, range(1, i + 1), 1))

    res = []

    for j in range(3, 1000000):
        digits = [int(x) for x in list(str(j))]
        tempSum = 0
        for dig in digits:
            tempSum += fact[dig]

        if tempSum == j:
            res.append(j)

    print(sum(x for x in res))


if __name__ == '__main__':
    main()
