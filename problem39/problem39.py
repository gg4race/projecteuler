def main():
    pMax = 1001
    perim = 0
    counter = 0
    maxCount = 0
    maxPerim = 0
    currPerim = 0
    sidesSet = set()
    while currPerim <= pMax:
        sidesSet.clear()
        counter = 0
        for i in range(1, currPerim):
            for j in range(1, currPerim - i):
                k = (i ** 2 + j ** 2) ** 0.5

                perim = i + j + k
                # print(perim)
                if perim == currPerim and i not in sidesSet:  # and (j in sidesSet == False) :
                    #print("i is ", i)
                    #print("j is ", j)
                    #print("k is ", k)
                    sidesSet.add(i)
                    sidesSet.add(j)
                    sidesSet.add(k)
                    counter += 1
                    if counter >= maxCount:
                        maxCount = counter
                        maxPerim = perim
        currPerim += 1

    print(maxCount)
    print(maxPerim)


if __name__ == '__main__':
    main()
