# Complete the greatestProduct method so that it'll find the greatest product of
# five consecutive digits in the given string of digits.

# For example:

# greatestProduct("123834539327238239583") // should return 3240

# The input string always has more than five digits.

# Adapted from Project Euler.

import numpy

def greatest_product(n):
    product = 0

    for i in range(0, len(n) - 4):
        new_product = numpy.prod([int(x) for x in n[i:(i+5)]])
        if new_product > product:
            product = new_product
            
    return product