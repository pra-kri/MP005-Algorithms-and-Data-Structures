# implement the random search for finding the minima of a function

import random


# will attempt to minimse a 3d fucntion wrt F(x,y)
# Himmeblau's function:
# F(x,y) = (x^2 + y - 11)^2 + (x + y^2 - 7)^2
# One local maxima: F = 181.617, at x=-0.270845, y=-0.923039
# 4 Local minima, all at F = 0.0
#    f(3.0, 2.0), f(-2.805118, 3.131312), f(-3.779310, -3.283186), f(3.584428, -1.848126)



def function_to_minimise(x, y):
    z = (x**2 + y - 11)**2 + (x + y**2 - 7)**2
    return z 
    

# search space for x = {-5, 5}, best for Himmelblau's Function


def random_search(in_function, space_start = -5, space_end=5):

    # goal: to minimise f(x,y)
    best= [float('inf'), 111.11, 111.11] #111.11 used as the initial case, so we know if the code hasnt worked properly....
    
    for i in range(0,10000):
        rand_x = random.uniform(space_start, space_end)
        rand_y = random.uniform(space_start, space_end)
        temp_result = in_function(rand_x, rand_y)
        if temp_result < best[0]:
            best[0] = temp_result
            best[1] = rand_x
            best[2] = rand_y
         
    
    return best
    
    
    
print(random_search(function_to_minimise))

"""
Notes: 
Each time the random_search() is run, the minima that I find is always close to 0, which is what is expected. Random search works quite well in this case, but is a large inefficiency to this algorithm:
    Worst case time-efficiency: technically, since the algorithm doesnt store previous search value, you could theoretically keep generating the same random numbers again and again and again... giving this a worst case complexity of O(infinity)...
"""
