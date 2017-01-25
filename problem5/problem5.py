def main():

    i = 2

    #loop through integers to and make sure multiple is evenly divisible by each
    for j in (range(2, 21)):
        if i % j != 0:
            #if not evenly divisible, increase multiple until divisible
            for k in range(2, 21):
                if (i * k) % j == 0:
                    i *= k
                    break
    print (i)


if __name__ == '__main__':
    main()
