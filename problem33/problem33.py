def main():
    from fractions import Fraction

    def checkSimp(nom, denom):
        for i in (0, 1):
            tempNom = list(str(nom))[i]
            for j in (0, 1):
                if list(str(denom))[j] == tempNom:
                    if i == 0:
                        leftoverNom = list(str(nom))[1]
                    else:
                        leftoverNom = list(str(nom))[0]
                    if j == 0:
                        leftoverDenom = list(str(denom))[1]
                        return ([leftoverNom, leftoverDenom])
                    else:
                        leftoverDenom = list(str(denom))[0]
                        return ([leftoverNom, leftoverDenom])

        return None

    nomProd = 1
    denomProd = 1
    for denom in range(10, 100):
        for nom in range(10, denom):
            tempList = checkSimp(nom, denom)
            if nom % 10 != 0 or denom % 10 != 0:
                if tempList is not None:
                    if int(tempList[1]) != 0:
                        if Fraction(nom, denom) == Fraction(int(tempList[0]), int(tempList[1])):
                            nomProd *= Fraction(denom, nom).denominator
                            denomProd *= Fraction(nom, denom).denominator

    print(Fraction(nomProd, denomProd).denominator)


if __name__ == '__main__':
    main()
