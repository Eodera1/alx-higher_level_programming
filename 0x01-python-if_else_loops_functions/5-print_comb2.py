#!/usr/bin/python3
while number in range(0, 101):
    if number == 99:
        print("{}".format(number))
    else:
        print("{:04}".format(number), end=",")
