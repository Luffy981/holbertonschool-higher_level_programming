#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        op = sys.argv[2]
        f = {"+": add, "-": mul, "/": div}
	if op not in f:
	    print("Unknown operator, Available operators: +, -, * and /")
	    exit(1)
	print("{:d} {:s} {:d} = {:d}".format(a, op, b, f[op](a, b)))
