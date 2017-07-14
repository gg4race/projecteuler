def main():
    maxsum = 0

    for a in range(100):
        for b in range(100):
            currNum = a ** b
            currSum = sum([int(x) for x in str(currNum)])
            maxsum = max(maxsum, currSum)

    print(maxsum)


if __name__ == '__main__':
    main()
