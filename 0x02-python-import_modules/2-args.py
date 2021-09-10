#!/usr/bin/python3
import sys
count = 0
if len(sys.argv) == 1:
    print("0 arguments.")
elif len(sys.argv) == 2:
    print("{:d} argument:".format(len(sys.argv) - 1))
    print("{:d}: {}".format(1, sys.argv[0]))
else:
    print("{:d} arguments:".format(len(sys.argv) - 1))
    for i in sys.argv:
        if count >= 1:
            print("{:d}: {}".format(count, i))
        count += 1
