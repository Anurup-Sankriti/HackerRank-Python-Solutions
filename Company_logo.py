#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def arraychoose(array):
    same_array = [array[0][0]]
    to_remove_array = []
   
    for i in range(1,len(array)):
        if array[0][1] == array[i][1]:
            same_array.append(array[i][0])
   
    same_array = sorted(same_array)
    
    alp = same_array[0]
    
    for i in range(0,len(same_array)):
        if array[i][0] == alp:
            alp_num = array[i][1]
    print(alp, alp_num)
    
    
    temp_list = [alp, alp_num]
    to_remove_array.append(temp_list)
            
              
    return [element for element in array if element not in to_remove_array]
if __name__ == '__main__' :
    s = input()
    my_list = []
    count_list = []
    count = 0
    for i in range(0, len(s)):
        my_list.append(s[i])
    
    count = Counter(my_list)
    
    unique_list = list(count.keys())
    for i in range(0,len(unique_list)):
        querry = unique_list[i]
        number = count[querry]
        
        temp_list = [querry, number]
        count_list.append(temp_list)
  
    sorted_list = sorted(count_list, key=lambda x: x[1], reverse=True)
  
    new_arr = arraychoose(sorted_list)
    new_arr2 = arraychoose(new_arr)
    new_arr2 = arraychoose(new_arr2)
    
    
