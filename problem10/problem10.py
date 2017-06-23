def main():
    #learn sieve of eratosthenes
    def eratosthenes2(n):
        multiples = set()
        for i in range(2, n + 1):
            if i not in multiples:
                yield i   #yield creates iterator, good for large set of values read only once
                multiples.update(range(i * i, n + 1, i))

    print(sum(eratosthenes2(2000000)))


if __name__ == '__main__':
    main()
