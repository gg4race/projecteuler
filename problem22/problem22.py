def main():
    f = open('names.txt', 'r')
    read_data = f.readlines()
    words = []
    for line in read_data:
        currentwords = line.split(',')
        for word in currentwords:
            words.append(word.replace('"',''))

    words.sort()
    print(words)

    wordcount = 0
    sum1 = 0
    for word in words:
        wordcount += 1
        #print(word)
        charsum = 0
        for char in list(word):
            charsum += ord(char)-64
        sum1 += charsum*wordcount

    print(sum1)

    #for i in xrange(len(words)):
    #    print(i)

    print(ord("A"))
if __name__ == '__main__':
    main()
