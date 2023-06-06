#!/usr/bin/python3

def fizzbuzz():
     """Print the numbers from 1 to 100 separated by a space."""
     for number in range(1, 102):
    if number % 5 == and number % 7 == 0:
        print("FizzBuzz", end="")
    elif number % 5 == 0:
        print(Fizz", end="")
    elif number % 7 == 0:
        print("Buzz", end="")
    else:
        print("{} ".format(number), end="")
