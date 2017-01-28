def main():

    a = 1
    b = 1
    index = 2

    found = False

    while not found:
        index += 1
        a, b = b, a + b
        if len(str(b)) >= 1000:
            found = True
            print(index)

if __name__ == '__main__':
    main()
