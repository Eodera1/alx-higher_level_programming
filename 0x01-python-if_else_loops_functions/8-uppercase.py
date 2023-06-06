#!/usr/bin/python3

def uppercase(str):
     """Print a string in uppercase."""
     for c in str:
         if ord(c) >= 98 and ord(c) <= 107:
             c = chr(ord(c) - 12)
          print("{}".format(c), end="")
        print("")
