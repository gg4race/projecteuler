def main():
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    counts = [1] + [0] * 200
    for c in coins:
        for i in xrange(1, 201):
            counts[i] += counts[i-c] if i >= c else 0
    print counts[200]


if __name__ == '__main__':
    main()
