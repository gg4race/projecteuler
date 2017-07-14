def main():
    p = set(n * ((3 * n) - 1) / 2 for n in range(2, 4000))
    for i in p:
        for j in p:
            if i + j in p and j - i in p:
                x = i - j
                res = min(res, x)
            else:
                continue
    print ("Answer = ", res)


if __name__ == '__main__':
    main()
