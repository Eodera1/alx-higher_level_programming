#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(f"{number:g} is positive")
elif number == 0:
print(f"{number:g} is zero")
else:
    print(f"{number:g} is negative")
