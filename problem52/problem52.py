def main():
    import collections
    found = False
    i = 11
    while found == False:
        list1 = list(str(i))
        list2 = list(str(i * 2))
        if collections.Counter(list1) == collections.Counter(list2):
            # found = True
            list3 = list(str(i * 3))
            if collections.Counter(list1) == collections.Counter(list3):
                # found = True
                list4 = list(str(i * 4))
                if collections.Counter(list1) == collections.Counter(list4):
                    # found = True
                    list5 = list(str(i * 5))
                    if collections.Counter(list1) == collections.Counter(list5):
                        # found = True
                        list6 = list(str(i * 6))
                        if collections.Counter(list1) == collections.Counter(list6):
                            found = True
        i += 1

    print(i - 1)


if __name__ == '__main__':
    main()
