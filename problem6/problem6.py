def main():

    xsum = sum(range(1, 101))
    squaredSum = sum(i * i for i in range(1, 101))
    print(xsum * xsum - squaredSum)


if __name__ == '__main__':
    main()
