def main():
    res = set()
    for i in range(1, 100):
        for j in range(1, 100):
            currPow = pow(i, j)
            if len(str(currPow)) == j:
                res.add(currPow)

    print(len(res))


if __name__ == '__main__':
    main()
