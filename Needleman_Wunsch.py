"""
Implement the Needleman-Wunsch algo. (The Optimal Matching algorithm)

- Commonly used for aligning protein or DNA sequences, in bioinformatics.
- Type of 'Dynamic programming' algo, where previously solved sub-problems' solutions are used to help solve problems later.

- The higher the score returned from the algorithm, the better the match, essentially.
- Highest possible score = length of the longest being compared.

- Our scoring system: if there is a match in letters: score += 1
                        if there is a mismatch, then score -= 1
                        

References:
https://en.wikipedia.org/wiki/Needleman%E2%80%93Wunsch_algorithm

"""

import numpy as np

def Needleman_Wunsch(s1, s2):
    string1 = str(s1)
    string2 = str(s2)
    
    len1 = len(string1)
    len2 = len(string2)
    
    aaa = np.zeros(shape = (len1 + 1, len2 + 1))
    
    # set top row, and left-most column to be ranging from 0 to -(length of strings).
    for i in range(0,len1 + 1):
        aaa[i,0] = -i  
    for j in range(0, len2 + 1):
        aaa[0, j] = -j

    for i in range(1, len1+1):
        for j in range(1, len2+1):
            if string1[i-1] == string2[j-1]:
                match = aaa[i-1, j-1] +1
                insert_del1 = aaa[i-1, j] - 1
                insert_del2 = aaa[i, j-1] - 1
                
                temp_list = [match, insert_del1, insert_del2]
                temp_max = max(temp_list)
                
                aaa[i, j] = temp_max
            else:
                mismatch = aaa[i-1, j-1] - 1
                insert_del1 = aaa[i-1, j] - 1
                insert_del2 = aaa[i, j-1] - 1
                
                temp_list = [mismatch, insert_del1, insert_del2]
                temp_max = max(temp_list)
                aaa[i,j] = temp_max
    
    
    return aaa, aaa[-1,-1]


print(Needleman_Wunsch('GATTACA','GCATGCU'))
print(Needleman_Wunsch('GATTACA','zzzzzzzzz'))
print(Needleman_Wunsch('GATTACA','GATTACA'))
