def main():
    def ispalindrome(x):
        arr = [i for i in str(x)]
        return arr == arr[::-1]

    def flip(num):
        arr = [x for x in str(num)]
        return int(''.join(arr[::-1]))

    lychrels = []

    for i in range(10, 10000):
        iter = 1
        currsum = i + flip(i)
        found = ispalindrome(currsum)
        while iter <= 50 and not found:
            currsum = currsum + flip(currsum)
            found = ispalindrome(currsum)
            if found:
                break
            iter += 1
        if not found:
            lychrels.append(i)
    print(len(lychrels))


if __name__ == '__main__':
    main()
