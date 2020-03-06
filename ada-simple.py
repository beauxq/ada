"""
'simple' means this is for a simpler machine, which means this code is more complex than ada.py
ada.py has ada's original operations which are simpler than this

Ada assumed having math operations + - * /
Ada also assumed having data structures for non-integers. (Bernoulli numbers are rational numbers.)
I was doing research about a simple machine that has only operations + and - and only for integers.
So I was thinking about what it would take to run Ada's program on this simpler machine.

First, multiplication can be implemented with a software subroutine using addition.
Next, rational numbers can be represented with 2 integers, so we can translate the operations
on rational numbers to a sequence of operations on integers.
I add "n" to variable names for numerators and "d" for denominators.
I add "i" to variable names if the integer data structure suffices for that variable.
Lastly, given these previous solutions, the problem of division has disappeared.
(Dividing by 2/3 is just multiplying by 3/2.)

Reducing fractions is required in order to not quickly get into ridiculous
processing times and ridiculous bit lengths per integer.

Without reducing fractions:
Calculating B8 (the 4th non-trivial Bernoulli number) requires integers >32 bits
and ~20 seconds of processing time on a core i7.
Calculating B10 (the 5th non-trivial Bernoulli number) requires integers >64 bits
and I don't know how much processing time. I stopped it at 7 hours.

The machine I was thinking of is 8 bits, so I would like to see how far I can get with that.
Obviously B12 (-691 / 2730) has both a numerator and denominator that don't fit in 8 bits.
So I guess B10 is the goal.

Reducing fractions brings back the problem of division that had disappeared.
But that's not hard to implement in software, just like multiplication.
We can get to B6 by simply reducing some of the fractions after calculating them.
But that's not enough for B8 and B10.
We'll need another subroutine for adding 2 fractions.
The most common (and most efficient on most computers) method for finding
the lowest common denominator involves multiplying the denominators,
but that completely defeats the purpose if we need to stay in 8 bits.

On this machine it is more efficient to find the lowest common denominator in the
process of adding the fractions, instead of as a first step to adding the fractions.

In the calculations of B10, there's one point when the multiplication of 2 fractions
is 7/5 * 30/1 = 210/5.
210 is an overflow in 8-bit signed integers.
The result can be reduced to fit in 8 bits (42/1), but it can't be reduced IN 8 bits.
Overflow can be avoided by doing a cross-reduction before the multiplication.
Reduce 30/5 and 7/1 to 6/1 and 7/1, then multiply to get the already reduced 42/1.
I guess it's kind of cheating to write the program already knowing all the results
of everything it needs to do, but I'm only doing this cross-reduction for the one
place where I know it would otherwise overflow.
It could be done for every fraction multiplication, but in most places
I think it would add more memory requirements and processing for no benefit.
I'm not sure about that. It could be less processing in some cases,
but it would add more memory requirements either way.
"""

PRINT_ALL_RESULTS = False


def report_results(*argv):
    """ debugging """
    if PRINT_ALL_RESULTS:
        print(*argv)


def multiply(a, b):
    """ multiply two integers (using only addition and subtraction) """
    if a < 0:  # need to be able to multiply with negative numbers
        # swap both signs
        a = 0 - a
        b = 0 - b
    to_return = 0
    while a > 0:
        to_return = to_return + b
        a = a - 1
    if to_return > 127 or to_return < -128:
        report_results("warning: multiply result", to_return, "won't work in 8 bits")
    return to_return


def add_fractions(an, ad, bn, bd):
    # find LCD at the same time as multiplying the numerators
    alcd = ad
    blcd = bd
    anm = an  # a numerator multiplied
    bnm = bn  # b numerator multiplied
    while alcd != blcd:
        if alcd < blcd:
            alcd = alcd + ad
            anm = anm + an
        else:
            blcd = blcd + bd
            bnm = bnm + bn
    return anm + bnm, alcd


def divide(a, b):
    """
    integer division (using only addition and subtraction)
    only works with positive b
    """
    a_sign = 1  # 1 or -1
    if a < 0:
        a_sign = -1
        a = 0 - a
    count = 0
    while a >= b:
        a = a - b
        count = count + 1
    return multiply(a_sign, count)


def gcd(a, b):
    """ greatest common divisor (a and b both positive) """
    # I want to implement this without a stack (no recursion)
    # just in case this simpler machine can't handle a stack
    # (no dynamic memory management, using all the memory for one of each function call)
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def reduce(n, d):
    """ reduce fraction """
    # It might be enough reduction to only ever reduce v13
    # which means it could be optimized to hard code the memory addresses of v13
    # instead of passing parameters and return values
    # 
    # In 8 bits, reducing only v13 is enough to calculate B4, but not enough for B6
    if d < 0:
        # swap both signs
        n = 0 - n
        d = 0 - d
    positive_n = n
    if n < 0:
        positive_n = 0 - positive_n
    divisor = gcd(positive_n, d)
    return divide(n, divisor), divide(d, divisor)


def f(v20n, v20d):
    """ v20 is list of result variables - input data starting with 0 and ending with 0
    Between these zeros, it contains the already known Bernoulli numbers starting with 1/6
    Ada's variable names for this are v21, v22, v23, etc.
    v20n is the numerators, v20d is the denominators """

    # initialization of data and working variables
    v1i = 1  # a constant
    v2i = 2  # a constant
    v3i = len(v20n) - 1  # indicates which Bernoulli number is being calculated
    # Ada shows all of the working variables initialized to 0
    # but only 2 of those initializations matter
    v7i = 0
    v13n = 0

    # all of the (unnecessary) initializations:
    # commented ones are necessary and done above
    # v1i = 1
    # v2i = 2
    # v3i = len(v20n) - 1
    v4i = 0
    v5i = 0
    v6i = 0
    # v7i = 0
    v8n = 0
    v8d = 1
    v9n = 0
    v9d = 1
    v10i = 0
    v11n = 0
    v11d = 1
    v12n = 0
    v12d = 1
    # v13n = 0
    v13d = 1
    # 18 working variables


    # 1
    v4i = multiply(v2i, v3i)
    v5i = v4i
    v6i = v4i
    report_results(v4i)

    # 2
    v4i = v4i - v1i
    report_results(v4i)
    
    # 3
    v5i = v5i + v1i
    report_results(v5i)

    # 4
    # v11 = v4 / v5  # originally v11 = v5 / v4
    v11n = v4i
    v11d = v5i
    report_results(v11n, "/", v11d)

    # 5
    # v11 = v11 / v2
    v11d = multiply(v11d, v2i)
    report_results(v11n, "/", v11d)

    # 6
    # v13 = v13 - v11
    v13n = v13n - v11n  # v13n is initialized to 0
    v13d = v11d
    v13n, v13d = reduce(v13n, v13d)
    # A0 = v13
    report_results(v13n, "/", v13d)

    # 7
    v10i = v3i - v1i  # v10 is a control variable, not used in any calculations that go to the output
    report_results(v10i)

    # 8
    v7i = v2i + v7i
    report_results(v7i)

    # 9
    # v11 = v6 / v7
    v11n = v6i
    v11d = v7i
    # A1 = v11
    report_results(v11n, "/", v11d)

    # 10
    # v12 = v20[1] * v11
    v12n = multiply(v20n[1], v11n)
    v12d = multiply(v20d[1], v11d)
    # B1A1 = v12
    report_results(v12n, "/", v12d)

    # 11
    # v13 = v12 + v13
    v13n, v13d = add_fractions(v12n, v12d, v13n, v13d)
    v13n, v13d = reduce(v13n, v13d)
    report_results(v13n, "/", v13d)

    # 12
    v10i = v10i - v1i
    report_results(v10i)

    while v10i > 0:  # "Here follows a repetition of Operations thirteen to twenty-three."
        
        # 13
        v6i = v6i - v1i
        report_results(v6i)

        # 14
        v7i = v1i + v7i
        report_results(v7i)

        # 15
        # v8 = v6 / v7
        v8n = v6i
        v8d = v7i
        v8n, v8d = reduce(v8n, v8d)
        report_results(v8n, "/", v8d)

        # 16
        # v11 = v8 * v11
        v11nr, v8dr = reduce(v11n, v8d)  # this just needed to not overflow in 8 bits when calculating B10 (210 as 8-bit signed int)
        v11n = multiply(v8n, v11nr)
        v11d = multiply(v8dr, v11d)
        v11n, v11d = reduce(v11n, v11d)
        report_results(v11n, "/", v11d)

        # 17
        v6i = v6i - v1i
        report_results(v6i)

        # 18
        v7i = v1i + v7i
        report_results(v7i)

        # 19
        # v9 = v6i / v7i
        v9n = v6i
        v9d = v7i
        v9n, v9d = reduce(v9n, v9d)
        report_results(v9n, "/", v9d)

        # 20
        # v11 = v9 * v11
        v11n = multiply(v9n, v11n)
        v11d = multiply(v9d, v11d)
        v11n, v11d = reduce(v11n, v11d)
        # A3 = v11
        report_results(v11n, "/", v11d)

        # 21
        # v12 = v20[v3i - v10i] * v11
        v12n = multiply(v20n[v3i - v10i], v11n)
        v12d = multiply(v20d[v3i - v10i], v11d)
        v12n, v12d = reduce(v12n, v12d)
        # B3A3 = v12 (B5A5...)
        report_results(v12n, "/", v12d)

        # 22
        # v13 = v12 + v13
        v13n, v13d = add_fractions(v12n, v12d, v13n, v13d)
        v13n, v13d = reduce(v13n, v13d)
        report_results(v13n, "/", v13d)

        # 23
        v10i = v10i - v1i
        report_results(v10i)

    # 24
    # v20[v3i] = v20[v3i] - v13  # originally v20[v3] = v13 + v20[v3]
    v20n[v3i] = v20n[v3i] - v13n  # v20n[v3i] is initialized to 0
    v20d[v3i] = v13d

    # 25
    v3i = v1i + v3i  # this is just preparation to calculate the next Bernoulli number

    return v20n[v3i - 1], v20d[v3i - 1]


def bn(n):
    """ returns Bernoulli number 2n
        returns a string for n < 1 """

    if n < 1:
        return "B0 = 1, B1 = ±1/2"

    v20n = [0, 1]
    v20d = [1, 6]
    what_we_have_so_far = 1

    while what_we_have_so_far < n:
        v20n.append(0)
        v20d.append(1)

        f(v20n, v20d)

        what_we_have_so_far += 1

    return v20n[-1], v20d[-1]  # last item


def main():
    try:
        n = int(input("Bernoulli number 2n:\n n? "))
        print(bn(n))
    except ValueError:
        print("need integer")


if __name__ == "__main__":
    main()
