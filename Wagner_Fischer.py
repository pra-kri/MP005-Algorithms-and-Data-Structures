"""
Implement the Wagner-Fischer algorithm to calculate edit-distance between 2 strings.

Basically, the algorithm calculates how many changes you need to make to string1 in order to make it identical to string2.
A 'change' is defined by any of the following: a letter replacement, a letter deletion, a letter insertion.

Possible uses for the algorithm:
    - DNA sequence similarity checking
    - spell-checking - to determine what the typo might actually mean
    - 
"""

import numpy as np



def Wagner_Fischer(s1, s2):
    string1 = str(s1)
    string2 = str(s2)
    len1 = len(string1)
    len2 = len(string2)
    
    aaa = np.zeros(shape = (len1 + 1, len2 + 1))

    # set top row, and left-most column to be ranging from 0 to length of words.
    for i in range(0,len1 + 1):
        aaa[i,0] = i  
    for j in range(0, len2 + 1):
        aaa[0, j] = j
        
    # go through each element of the numpy array, and apply the algorithm.
    # At that specificpoint in the array, if the letters from both strings match, then that element of the array will be identical to the value in the element that is in the top-left direction to it.
    # Otherwise, it will be the smallest value from the following (Top + 1, left + 1, or top-left + 1)
    for j in range(1, len2 + 1):
        for i in range(1, len1 + 1):
            if string1[i-1] == string2[j-1]:
                aaa[i, j] = aaa[i-1, j-1]
            else:
                
                temp_list = [aaa[i-1, j] + 1, aaa[i, j-1] + 1, aaa[i-1, j-1] + 1]
                aaa[i, j] = min(temp_list)
                
    minimum_edit_dist = aaa[-1, -1]
    
    return minimum_edit_dist
    
print(Wagner_Fischer("abcdefghij","aaaaaaaaij"))
print(Wagner_Fischer("computer","company"))
print(Wagner_Fischer("ATGCTACGACA","GATTACAATA"))

