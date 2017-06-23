def main():
    res = set()

    for i in range(2, 101):
        for j in range(2, 101):
            curr = i ** j
            res.add(curr)

    print(len(res))


if __name__ == '__main__':
    main()
