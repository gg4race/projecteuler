def main():
    def euler92(limit):
        # Let sumsq uphold the invariant that the nth element contains
        # the sum of the squares of the digits of n, or better yet, a
        # value somewhere along its reduction chain.

        # Start with the base case: chain[0] = sum(0 * 0) = 0.
        # Also preallocate many unknowns...
        sumsq = [sum((0 * 0,))] + [None] * limit

        # ... and fill them in.  Note how we reuse previous sums!
        for i in range(1 + limit):
            sumsq[i] = (i % 10) ** 2 + sumsq[i // 10]

        # Keep reducing each element until everything has converged
        # on either 1 or 89.
        all_converged = False
        while not all_converged:
            all_converged, eighty_nines = True, 0
            for i in range(1, 1 + limit):
                if sumsq[i] == 1:
                    pass
                elif sumsq[i] == 89:
                    eighty_nines += 1
                else:
                    all_converged = False
                    # sumsq[sumsq[i]] is a quick way to calculate
                    # the sum of the squares of the digits, and maybe
                    # even skip a few steps down the chain.
                    sumsq[i] = sumsq[sumsq[i]]
        return eighty_nines

    print (euler92(10000000))


if __name__ == '__main__':
    main()
