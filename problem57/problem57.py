def main():
    # p
    p = 1

    # q
    q = 1

    # counter
    counter = 0

    # 1000 iterations
    for i in xrange(1000):
        a1 = p + 2 * q
        b1 = p + q
        if len(str(a1)) > len(str(b1)):
            counter += 1
        p = a1
        q = b1

    # printing the counter
    print counter


if __name__ == '__main__':
    main()
