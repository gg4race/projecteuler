import math

def main():

    # think of each right step as 1, down step as -1, you will start from 0 and end at 0,
    # for 20x20 grid, this is a permutation with repetition. 40 elements, 20 of 1's, 20 of -1's

    print(int(math.factorial(40) / math.factorial(20) / math.factorial(20)))

    grid = [[0] * 21 for i in xrange(21)]  #21 horizontally then vertically
    grid[0][0] = 1
    for i in xrange(21):
        for j in xrange(21):
            if i > 0:
                grid[i][j] += grid[i-1][j]
            if j > 0:
                grid[i][j] += grid[i][j-1]
    print grid[20][20]


if __name__ == '__main__':
    main()
