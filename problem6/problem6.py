def main():
    sum = 0
    squaredSum = 0

    #get sum of integers and sum of squares of integers
    for i in range(1, 101):
        sum, squaredSum = sum + i, squaredSum + i * i

    print(sum * sum - squaredSum)


if __name__ == '__main__':
    main()
