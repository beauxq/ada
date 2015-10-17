from fractions import Fraction

PRINT_ALL_RESULTS = False


def f(v20):
    """ v20 is list of input data starting with 0 and ending with 0
    Between these zeros, it contains the already known Bernoulli numbers starting with 1/6
    Ada's variable names for this are v21, v22, v23, etc. """

    v1 = Fraction(1)
    v2 = Fraction(2)
    v3 = Fraction(len(v20) - 1)
    v7 = Fraction(0)
    v13 = Fraction(0)

    # 1
    v4 = v2 * v3
    v5 = v4
    v6 = v4
    if PRINT_ALL_RESULTS:
        print(v4)

    # 2
    v4 = v4 - v1
    if PRINT_ALL_RESULTS:
        print(v4)
    
    # 3
    v5 = v5 + v1
    if PRINT_ALL_RESULTS:
        print(v5)

    # 4
    v11 = v4 / v5  # originally v11 = v5 / v4
    if PRINT_ALL_RESULTS:
        print(v11)

    # 5
    v11 = v11 / v2
    if PRINT_ALL_RESULTS:
        print(v11)

    # 6
    v13 = v13 - v11
    # A0 = v13
    if PRINT_ALL_RESULTS:
        print(v13)

    # 7
    v10 = v3 - v1
    if PRINT_ALL_RESULTS:
        print(v10)

    # 8
    v7 = v2 + v7
    if PRINT_ALL_RESULTS:
        print(v7)

    # 9
    v11 = v6 / v7
    # A1 = v11
    if PRINT_ALL_RESULTS:
        print(v11)

    # 10
    v12 = v20[1] * v11
    # B1A1 = v12
    if PRINT_ALL_RESULTS:
        print(v12)

    # 11
    v13 = v12 + v13
    if PRINT_ALL_RESULTS:
        print(v13)

    # 12
    v10 = v10 - v1
    if PRINT_ALL_RESULTS:
        print(v10)

    while v10 > 0:  # "Here follows a repetition of Operations thirteen to twenty-three."
        
        # 13
        v6 = v6 - v1
        if PRINT_ALL_RESULTS:
            print(v6)

        # 14
        v7 = v1 + v7
        if PRINT_ALL_RESULTS:
            print(v7)

        # 15
        v8 = v6 / v7
        if PRINT_ALL_RESULTS:
            print(v8)

        # 16
        v11 = v8 * v11
        if PRINT_ALL_RESULTS:
            print(v11)

        # 17
        v6 = v6 - v1
        if PRINT_ALL_RESULTS:
            print(v6)

        # 18
        v7 = v1 + v7
        if PRINT_ALL_RESULTS:
            print(v7)

        # 19
        v9 = v6 / v7
        if PRINT_ALL_RESULTS:
            print(v9)

        # 20
        v11 = v9 * v11
        # A3 = v11
        if PRINT_ALL_RESULTS:
            print(v11)

        # 21
        v12 = v20[int(v3 - v10)] * v11
        # B3A3 = v12 (B5A5...)
        if PRINT_ALL_RESULTS:
            print(v12)

        # 22
        v13 = v12 + v13
        if PRINT_ALL_RESULTS:
            print(v13)

        # 23
        v10 = v10 - v1
        if PRINT_ALL_RESULTS:
            print(v10)

    # 24
    v20[int(v3)] = v20[int(v3)] - v13  # originally v20[int(v3)] = v13 + v20[int(v3)]

    # 25
    v3 = v1 + v3

    return v20[int(v3 - 1)]


def bn(n):
    """ returns Bernoulli number 2n
        returns a string for n < 1 """

    if n < 1:
        return "B0 = 1, B1 = ±1/2"

    v20 = [0, Fraction("1/6")]
    what_we_have_so_far = 1

    while what_we_have_so_far < n:
        v20.append(0)

        f(v20)

        what_we_have_so_far += 1

    return v20[-1]  # last item


def main():
    try:
        n = int(input("Bernoulli number 2n:\n n? "))
        print(bn(n))
    except ValueError:
        print("need integer")


if __name__ == "__main__":
    main()
