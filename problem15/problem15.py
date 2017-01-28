import math

def main():

    # think of each right step as 1, down step as -1, you will start from 0 and end at 0,
    # for 20x20 grid, this is a permutation with repetition. 40 elements, 20 of 1's, 20 of -1's

    print(int(math.factorial(40) / math.factorial(20) / math.factorial(20)))


if __name__ == '__main__':
    main()
