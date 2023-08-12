#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    le = len(sys.argv) - 1
    if le != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)
    else:
        argv = sys.argv[1:]
        a = int(argv[0])
        b = int(argv[2])
        opp = argv[1]
        if opp == "+":
            print('{:d} + {:d} = {:d}'.format(a, b, (add(a, b))))
        elif opp == "-":
            print('{:d} - {:d} = {:d}'.format(a, b, (sub(a, b))))
        elif opp == "*":
            print('{:d} * {:d} = {:d}'.format(a, b, (mul(a, b))))
        elif opp == "/":
            print('{:d} / {:d} = {:d}'.format(a, b, (div(a, b))))
        else:
            print('Unknown operator. Available operators: +, -, * and /')
            sys.exit(1)
