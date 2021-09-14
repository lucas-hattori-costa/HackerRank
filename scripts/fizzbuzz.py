#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    for i in range(1,n+1):
        fizz = (i % 3 == 0)
        buzz = (i % 5 == 0)
        if not fizz:
            if not buzz:
                print(i)
            else:
                print('Buzz')
        else:
            if buzz:
                print('FizzBuzz')
            else:
                print('Fizz')

                
            
            

if __name__ == '__main__':