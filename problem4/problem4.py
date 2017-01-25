def main():
    # loop through pairs of integers and return largest palindrome product

    a = 999

    def isPalindrome(a, b):

        product = str(a * b)
        endIndex = 0
        isPalindrome = True

        if (len(product) % 2 == 0):
            endIndex = int(len(product) / 2)
        else:
            endIndex = int((len(product) - 1) / 2)

        for i in range(0, endIndex):
            if (product[i] != product[len(product) - i - 1]):
                isPalindrome = False
                break
            i += 1

        return isPalindrome

    palindrome = 0
    #loop through pairs of numbers
    while a >= 100:
        #reset b for each a
        b = 999
        while b >= 100:
            if (isPalindrome(a, b)):
                palindrome = max(palindrome, a * b)
            b -= 1
        a -= 1

    print(palindrome)


if __name__ == '__main__':
    main()
