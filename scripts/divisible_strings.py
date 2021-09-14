#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findSmallestDivisor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#

def findSmallestDivisor(s, t):
    # Write your code here
    if s.replace(t,''):
        return -1
    
    response = len(t)

    for i in range(1,len(t)//2+1):
        sub_t = t[:i]
        print(sub_t)
        if isDivisor(t,sub_t) and isDivisor(s,sub_t):
            response = len(sub_t)

    return response


def isDivisor(full_string,sub_string) -> bool:
    if full_string.replace(sub_string,''):
        return False
    else:
        return True

if __name__ == '__main__':
    # s = 'lrbblrbb'
    # t = 'lrbb'

    # s = 'rbrb'
    # t = 'rbrb'

    s = 'abcabcabcabcabcabc'
    t = 'abcabcabc'

    result = findSmallestDivisor(s, t)

    print(result)
