from fractions import Fraction

PRINT_ALL_RESULTS = False


def report_results(*argv):
    """ debugging """
    if PRINT_ALL_RESULTS:
        print(*argv)



def f(v20):
    """ v20 is list of result variables - input data starting with 0 and ending with 0
    Between these zeros, it contains the already known Bernoulli numbers starting with 1/6
    Ada's variable names for this are v21, v22, v23, etc. """

    v1 = 1  # a constant
    v2 = 2  # a constant
    v3 = len(v20) - 1  # indicates which Bernoulli number is being calculated
    # Ada shows all of the working variables initialized to 0
    # but only 2 of those initializations matter
    v7 = 0
    v13 = Fraction(0)

    # 1
    v4 = v2 * v3
    v5 = v4
    v6 = v4
    report_results(v4)

    # 2
    v4 = v4 - v1
    report_results(v4)
    
    # 3
    v5 = v5 + v1
    report_results(v5)

    # 4
    v11 = Fraction(v4, v5)  # published with bug v11 = Fraction(v5, v4)
    report_results(v11)

    # 5
    v11 = v11 / v2
    report_results(v11)

    # 6
    v13 = v13 - v11
    # A0 = v13
    report_results(v13)

    # 7
    v10 = v3 - v1  # v10 is a control variable, not used in any calculations that go to the output
    report_results(v10)

    # 8
    v7 = v2 + v7
    report_results(v7)

    # 9
    v11 = Fraction(v6, v7)
    # A1 = v11
    report_results(v11)

    # 10
    v12 = v20[1] * v11
    # B1A1 = v12
    report_results(v12)

    # 11
    v13 = v12 + v13
    report_results(v13)

    # 12
    v10 = v10 - v1
    report_results(v10)

    while v10 > 0:  # "Here follows a repetition of Operations thirteen to twenty-three."
        
        # 13
        v6 = v6 - v1
        report_results(v6)

        # 14
        v7 = v1 + v7
        report_results(v7)

        # 15
        v8 = Fraction(v6, v7)
        report_results(v8)

        # 16
        v11 = v8 * v11
        report_results(v11)

        # 17
        v6 = v6 - v1
        report_results(v6)

        # 18
        v7 = v1 + v7
        report_results(v7)

        # 19
        v9 = Fraction(v6, v7)
        report_results(v9)

        # 20
        v11 = v9 * v11
        # A3 = v11
        report_results(v11)

        # 21
        v12 = v20[v3 - v10] * v11
        # B3A3 = v12 (B5A5...)
        report_results(v12)

        # 22
        v13 = v12 + v13
        report_results(v13)

        # 23
        v10 = v10 - v1
        report_results(v10)

    # 24
    v20[v3] = v20[v3] - v13  # published as v20[v3] = v13 + v20[v3]

    # 25
    v3 = v1 + v3  # this is just preparation to calculate the next Bernoulli number

    return v20[v3 - 1]


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
