def main():
    uniquePan = set()
    for multicland in range(1, 1999):
        for multiplier in range(multicland + 1, 1999):
            prod = multicland * multiplier
            digits = [int(x) for x in str(multicland) + str(multiplier) + str(prod)]
            if len(digits) == 9:
                digits.sort()
                pandigital = True
                i = 1
                while i <= len(digits) and pandigital == True:
                    if digits[i - 1] != i:
                        pandigital = False
                    i += 1
                if pandigital:
                    uniquePan.add(prod)

    print(sum(uniquePan))
    print(uniquePan)


if __name__ == '__main__':
    main()
