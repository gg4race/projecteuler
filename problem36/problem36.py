def main():
    def isPalindrome(in_arr):
        if len(in_arr) <= 1:
            return True
        else:
            if in_arr[0] != in_arr[len(in_arr) - 1]:
                return False
            else:
                return isPalindrome(in_arr[1:len(in_arr) - 1])

    tempSum = 0
    for i in range(1, 1000000):
        if isPalindrome(str(i)):
            if isPalindrome(str(bin(i))[2:]):
                tempSum += i

    print(tempSum)


if __name__ == '__main__':
    main()
