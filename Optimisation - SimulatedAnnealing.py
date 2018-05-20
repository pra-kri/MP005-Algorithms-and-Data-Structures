# implementing simulated annealing optimisation in Python, in order to minimise a function.
# This algo is inspired by the real-life heat-treating process of 'annealing', used to make materials more ductile and less hard.
# References: 
# http://www.cleveralgorithms.com/nature-inspired/physical/simulated_annealing.html
# http://katrinaeg.com/simulated-annealing.html


import random
import numpy as np
import matplotlib.pyplot as plt

# function to minimise: Himmeblau's function:
# F(x,y) = (x^2 + y - 11)^2 + (x + y^2 - 7)^2
# 
# 4 Local minima, all at F = 0.0
#    f(3.0, 2.0), f(-2.805118, 3.131312), f(-3.779310, -3.283186), f(3.584428, -1.848126)
#
# 1 local maxima: F = 181.617, at x=-0.270845, y=-0.923039.

# search space: x,y are each both between -5 and 5.
# Will attempt to MINIMISE the function.

space_start = -5
space_end = 5

def function_to_minimise(x, y):
    z = (x**2 + y - 11)**2 + (x + y**2 - 7)**2
    return z 

# need to define a cost-calculating function, so that you know how good or bad a solution is.
# as we are trying to minimise, the cost could just be the size of the actual F(x,y) at that point.

T_start = 100
T_end = 0.001
r = 0.95

def rand_gen_cost(input_function, space_start = -5, space_end = 5):
    
    best = [float('inf'), 111.11, 111.11] 
    # this is just a temporary 'best' solution, that will be overwritten soon.
    rand_x = random.uniform(space_start, space_end)
    rand_y = random.uniform(space_start, space_end)
    current_coords = (rand_x, rand_y)
    
    cost = input_function(rand_x, rand_y)
    
    #will return cost, x and y, as 3 separate parts
    return cost, rand_x, rand_y
    
#need to generate neighbouring points to the solution
def gen_neighbour(old_cost =None, old_x = None, old_y = None, input_function = function_to_minimise):
    # currently implemented without any 'memory' of old position, so is actually kind of an obsolete function for now...
    
    space_start = -4
    space_end = 4
    new_x = random.uniform(space_start, space_end)
    new_y = random.uniform(space_start, space_end)
    new_cost = input_function(new_x, new_y)
    
    return new_cost, new_x, new_y
        
        

print(rand_gen_cost(function_to_minimise))

def simulated_annealing(input_function):
    space_start = -4
    space_end = 4
    old_x = random.uniform(space_start, space_end)
    old_y = random.uniform(space_start, space_end)
    old_cost = input_function(old_x, old_y)
    
    T = 100
    T_end = 0.001
    r = 0.99
    
    while T > T_end:
        for i in range(60):
            neighbour_cost, neighbour_x, neighbour_y = gen_neighbour(input_function)
            transition_prob = np.exp((neighbour_cost - old_cost) / T)
            random_transition_threshold = random.random()
            
            if transition_prob > random_transition_threshold:
                old_x = neighbour_x
                old_y = neighbour_y
                old_cost = neighbour_cost
        T = T*r
    
    return old_cost, old_x, old_y

print(simulated_annealing(function_to_minimise))

#TODO: find + fix mistake...
