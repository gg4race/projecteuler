import math

def main():
    #very python specific syntax - trying to learn!
    print [a * b * (1000 - a - b) for a in xrange(1, 1000) for b in xrange(a, 1000) if a * a + b * b == (1000 - a - b) * (1000 - a - b)]


if __name__ == '__main__':
    main()
