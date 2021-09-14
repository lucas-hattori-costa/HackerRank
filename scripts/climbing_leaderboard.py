#!/bin/python3
## Source: https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    response = []
    ranked = list(dict.fromkeys(ranked)) # remove duplicates keeping the ordering
    for p in player:
        ranking = 0
        found=False
        for r in ranked:
            ranking+=1
            print(ranking, p, r)
            if p>=r:
                response.append(ranking)
                ranked.insert(ranking-1, p)
                found=True
                break
        if not found:
            response.append(ranking+1)
            ranked.insert(ranking, p)
        

    return response
            
def fastClimbingLeaderboard(ranked, player):
    ## attempt usign the same logic as merge sort
    raise NotImplementedError('Function yet to be implemented.')
    while True:
        if p == ranked[midpoint]:
            response.append()
        elif p > ranked[midpoint]:
            if p < ranked[midpoint-1]:
                response.append(midpoint)
                ranked.insert(midpoint-1, p)
                break
            else:
                midpoint = (n_ranked-midpoint)//2
        else:
            if p > ranked[midpoint+1]:
                response.append(midpoint)
                ranked.insert(midpoint+1, p)
                break
            else:
                midpoint = midpoint + (n_ranked-midpoint)//2
            
        
        

if __name__ == '__main__':
    ranked = [100, 90, 90, 80, 75, 60]
    player = [50, 65, 77, 90, 102]
    response = climbingLeaderboard(ranked,player)
    print(response)
