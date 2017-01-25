import math

def main():
    #find all the squares <=1000 first
    squares = {}
    i = 1
    target = 1000
    while i <= target:
        squares[i * i] = i * i
        i += 1

    product = 0
    #loop through to see if the sum of two squares is also a square
    def findProduct(target):
        for key in squares:
            for key2 in squares:
                if key != key2:
                    sum = squares[key] + squares[key2]
                    if sum in squares:
                        #if sum is a square, check if the three numbers add up to target
                        if math.sqrt(squares[key]) + math.sqrt(squares[key2]) + math.sqrt(sum) == target:
                            product = math.sqrt(squares[key]) * math.sqrt(squares[key2]) * math.sqrt(sum)
                            return product

    print(findProduct(target))


if __name__ == '__main__':
    main()
