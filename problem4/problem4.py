import math

def main():
    # loop through pairs of integers and return largest palindrome product

    a = 999

    def isPalindrome(a, b):

        product = str(a * b)
        endIndex = len(product)/2
        isPalindrome = True

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
''' more pro solution
    def ispal(n):
        s = str(n)
        return all(s[i] == s[len(s)-1-i] for i in xrange(len(s) / 2))

    print max(a * b for a in xrange(100, 1000) for b in xrange(100, 1000) if ispal(a * b))'''


if __name__ == '__main__':
    main()
