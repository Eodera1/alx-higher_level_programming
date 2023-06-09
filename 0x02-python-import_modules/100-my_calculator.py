#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    func = len(sys.argv) - 1
    if func != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    ops = sys.argv[2]
    if ops != '+' and ops != '-' and ops != '*' and ops != '/':
        print("Unknown operator. Available operators: /, *, + and and -")
        sys.exit(1)

    from calculator_1 import div, mul, add, sub

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if ops == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif ops == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif ops == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    else:
        print("{} / {} = {}".format(a, b, div(a, b)))
