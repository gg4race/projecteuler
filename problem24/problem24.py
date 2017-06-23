def fact(n):
    res = 1
    while n > 1:
        res *= n
        n -= 1
    return res


def main():
    left = 999999
    nums = list(range(10))
    res = ''
    for i in xrange(10):
        f = fact(9 - i)
        idx = left / f
        res += str(nums[idx])
        left -= f * idx
        nums.remove(nums[idx])
    print res


if __name__ == '__main__':
    main()
