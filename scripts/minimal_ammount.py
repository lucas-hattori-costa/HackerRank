#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'calculateAmount' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY prices as parameter.
#

def calculateAmount(prices):
    # Write your code here
    response = 0
    discount = prices[0]
    for i, p in enumerate(prices):
        if i == 0:
            response+=p
            continue
        response += max(p-discount,0)
        if p<discount:
            discount = p
    return response


if __name__ == '__main__':
    # prices = [1, 2, 3, 4]
    prices = [4, 9, 2, 3]

    result = calculateAmount(prices)
    print(result)
