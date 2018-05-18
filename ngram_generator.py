"""
n-gram generator - quick implementation 
(just working from scratch without much prior reading, so my implementation will probably be quite inefficient in terms of time and space taken....)

[/]- generate all possible letter-based n-grams that are present in a long string.
[/]- save them in a list of lists or something
[/]- figure out how to count the frequency of the n-grams that do appear. 

NOTE: currently the n-grams include spaces, since the n-grams are character based.
To make the n-gram generator work with words instead of characters, change the first line of the function and split the string by spaces. That way, each element of the list_of_atoms will be a word, instead of a character. 
"""
from collections import  Counter


long_string = "abcdefghijklmnopqrstuvwxyz"

def n_gram_printer(string_input, max_ngram_len = 29):
    list_of_atoms = list(string_input)
    # master_list contains ALL possible n-grams in the string.    
    master_list = []
    
    for ngramlength in range(1, max_ngram_len+1):
        #N_list will contain all n-grams of length (ngramlength)        
        N_list = []
        print("These are the n-grams for: n = " + str(ngramlength))        
        
        
        for start_position in range(len(list_of_atoms) - (ngramlength - 1)):       
            
            current_n_gram = list_of_atoms[start_position:start_position+ngramlength]
            current_str = ''.join(current_n_gram)
            N_list.append(current_str)
            # space-inefficient to save each n-gram as a list and then convert to a string, but just writing out in detail for clarity and future readability.
            
        
        
            print(current_str)
            # instead of printing, could also just save in a dictionary of list of lists.
            # dictionary will have key = ngram length, and value = list of all ngrams of that length.
        
        master_list.append(N_list)
        
    return master_list
    
    
    
# just testing out...
aaa = n_gram_printer(long_string)

# second example to test out...
bbb = n_gram_printer("This is a test sentence. String. List. Aaaaa", max_ngram_len=10)
bbb_count = Counter(x for xs in bbb for x in set(xs))


# to count how many times each n-gram turns up in a string...
c = Counter()
for med_list in bbb:
    for small_list in med_list:
        c[small_list] += 1
        
        #TODO: convert this into a function...
