def main():
    def pe38():
        for n in range(9487, 9213, -1):
            p = str(n * 1) + str(n * 2)
            pandigital = True
            digits = [int(x) for x in p]
            digits.sort()
            i = 1
            while i <= len(digits) and pandigital == True:
                if digits[i - 1] != i:
                    pandigital = False
                i += 1
            if pandigital:
                return p
        return "None found."

    print ("Largest 9-digit 1 to 9 pandigital number  =", pe38())


if __name__ == '__main__':
    main()
