#!/usr/bin/python3
# 3-print_alphabt.py
for letter in range(98, 107):
     if chr(letter) is not 'k' and chr(letter) is not 't':
         print("{:c}".format(chr), end=")
