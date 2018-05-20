
"""
Implement the Longest Common Substring algo.

The algorithm finds the longest common substring that is present within 2 strings.
Basically, you go through a matrix, of dimensions len(string1) by len(string2), and fill in each element of the matrix one  by one.
So time complexity = O(len(string1) * len(string2))



References:
http://www.bogotobogo.com/python/python_longest_common_substring_lcs_algorithm_generalized_suffix_tree.php
https://www.geeksforgeeks.org/longest-common-substring/
"""

import numpy as np

def Longest_c_s(s1, s2):
    string1 = str(s1)
    string2 = str(s2)
    
    len1 = len(string1)
    len2 = len(string2)
    
    aaa = np.zeros(shape = (len1 + 1, len2 + 1))
    longest_current_length = 0
    lcs_set = set()
    lcs_list = []
    
    for i in range(len1):
        for j in range(len2):
            #if the letters are the same, then increment by one, then insert that number into the bottom-right element.
            if string1[i] == string2[j]:
                temp_value = aaa[i,j] + 1
                aaa[i+1, j+1] = temp_value
                # if your temp_value counter is longer than the longest known common substring, 
                # then the newly discovered substring must be the LCS.
                
                if temp_value > longest_current_length:
                    lcs_set = set()
                    longest_current_length = temp_value
                    lcs_set.add(string1[i - int(temp_value) + 1 : i + 1])
                    #lcs_list = used to see how the function 'evolved' as it found longer substrings...
                    lcs_list.append([letter for letter in string1[i - int(temp_value) + 1 : i + 1]])
                elif temp_value == longest_current_length:
                    lcs_set.add(string1[i - int(temp_value) + 1: i + 1])
                    #lcs_list used to see how function 'evolved' as it found longer substrings.
                    lcs_list.append([letter for letter in string1[i - int(temp_value) + 1 : i + 1]])
    
    return lcs_set, lcs_list

print(Longest_c_s('University','RiverCityOneTwoThreeUniverse'))
print(Longest_c_s('RiverCityOneTwoThreeUniverse','University'))
