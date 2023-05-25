#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    ans = ""
    first_l = s[0].upper()
    ans = ans + first_l
    count = 0
    for i in range(1,len(s)):
        
        string = s[i].isalnum()
        if count == 0:
            ans = ans + str(s[i])
            #print(ans)
        else:
            if count == 1:
                #a = s[i].upper()
                ans = ans + str(s[i].upper())
                count = 0
        if string == False:
            count = 1
        
        
    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
