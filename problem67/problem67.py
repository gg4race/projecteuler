def main():
    triangle = open("p067_triangle.txt", "r")

    for c, line in enumerate(reversed(triangle.readlines())):
        currLine = [int(x) for x in line.replace('\n', '').split(' ')]
        if c>0:
            for i in range(len(currLine)):
                currLine[i] += max(prevLine[i], prevLine[i+1])

        prevLine = currLine
    print(currLine)

if __name__ == '__main__':
    main()
