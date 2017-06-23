def main():
    f = open("words.txt", "r")
    lines = f.readlines()
    words = []
    for line in lines:
        currentWords = line.split(',')
        for word in currentWords:
            words.append(word.replace('"',''))

    maxToTest = 500
    counter = 0
    nums = set()
    for i in range(1, maxToTest+1):
        nums.add(0.5*i*(i+1))

    for word in words:
        chars = list(word)
        sum0 = sum([ord(x)-64 for x in chars])
        if sum0 in nums:
            counter += 1


    print(counter)





if __name__ == '__main__':
    main()
