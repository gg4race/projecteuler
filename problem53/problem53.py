def main():
    import math
    res = 0
    for n in range(1, 101):
        for r in range(1, n + 1):
            c = math.factorial(n) / (math.factorial(r) * math.factorial(n - r))
            if c >= 1000000:
                res += 1
    print(res)


if __name__ == '__main__':
    main()
