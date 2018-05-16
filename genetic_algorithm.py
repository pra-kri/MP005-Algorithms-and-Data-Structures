
import random

"""
Target: to create a list of N numbers that sum up to X.
Evolve the lists through a genetic algorithm

Initially, generate a bunch of random lists.
The lists are 'aiming' to sum up to 100.
If they are far away from 100, they're most likely to die.
If they are close to 100, they will survive and reproduce.
Repeatedly make a large collection of lists reproduce, through multiple generations.
Finally, you should get a bunch of lists that are optimised to sum up to 100.

References: 
https://lethain.com/genetic-algorithms-cool-name-damn-simple/
"""
# e.g. If N = 4, and X = 100, the following lists would work:

example1 = [25, 25, 25, 25]
example2 = [1, 23, 70, 6]
example3 = [100, 0, 0, 0]

# create a function to generate random lists
def random_list(N = 4, mn = 0, mx = 100):
    
    lis1 = [random.randint(mn, mx) for i in range(N)]
    
    return lis1
    
test1 = random_list()
test2 = random_list()

# each list is an individual, and together they make our 'population'

# create a function to generate a list of lists - our 'population'

def create_population(population = 50, N1 = 4, mn1 = 0, mx1 = 100):
    # create, by default, 50 lists of length 4.
    ppl1 = [random_list(N1, mn1, mx1) for i in range(population)]
    
    return ppl1
    
pppp = create_population(100)


# our evolution criteria is that the list should sum up to 100.
# so we need a way to calculate how 'good' each list is.
# i.e. Calculate the FITNESS of each individual list.

def fitness_test(testee, target = 100):
    # fitness output is just the difference between the sum of list elements and the desired target (which is 100, by default)
    total = 0
    for element in testee:
        total += element
    
    return abs(target - total)


print(fitness_test(test1)) #yes works



# now define a function that can find the AVG fitness of an entire population
def ppl_fitness_test(test_population, pop_target = 100):
    
    population_size = len(test_population)
    total_fit_score = 0
    
    for element in test_population:
        total_fit_score += fitness_test(element, pop_target)
        
    avg_fitness = total_fit_score / population_size
    
    return avg_fitness
    
    
print(ppl_fitness_test(pppp))
# on average, the list sums up to 200. If our target is 100, the fitness score should avg at about 100. (yep, works)



# Fitness tests and generating populations works so far
# ------------------------------------------------------+
# Now we want to apply the actualy evolution step to the population


# evolution step will involve the following steps:
#   - We imagine that the bottom 70% of the population die
#   - So the top 30% stay, and they reproduce, to fill in the empty 70%
#   - Then, just apply a mass 'mutation' to all the individuals

# We can represent breeding by just combining half of each parent list, to make the child list.


def parent_combine(dad_list, mum_list):
    # assuming both parents are same len(), randomly combine elements from both parents until you create a child_list.
    length = len(dad_list)
    child_list = []
    
    for i in range(length//2):
        child_list.append(random.choice(dad_list))
        child_list.append(random.choice(mum_list))
        
    
        
    return child_list
  
print(parent_combine(test1, test2))# yep works


def ranked_survivors(population_to_rank, no_of_surv = 30):
    ranked = [(fitness_test(x, 100), x) for x in population_to_rank]
    # applied firness test ti each individual within population, and assigns each their score, and saves this as a list of tuples. The lower their score, the better they match the target. 
    ranked_1 = [x[1] for x in sorted(ranked)]
    # ranks the population by score, and only saves the 2nd element of each tuple.
    
    survivors = ranked_1[:no_of_surv]
    return survivors
    

ranked_population = ranked_survivors(pppp)

def new_generation(start_population):
    
    survivors = ranked_survivors(start_population)
    
    dad_list = [random.choice(survivors) for x in range(15)]
    mum_list = [x for x in survivors if x not in dad_list]
    
    next_gen = [x for x in survivors]# adds 30 survivors. 70 left.
    
    for i in range(70):
        temp_dad = random.choice(dad_list)
        temp_mum = random.choice(mum_list)
        
        temp_child = parent_combine(temp_dad, temp_mum)
        
        next_gen.append(temp_child)
        
    
    #TODO mutation bit
    for i in range(100):
        temp_individual = random.randint(0, 99)
        temp_position = random.randint(0, 3)
        next_gen[temp_individual][temp_position] = random.randint(0, 100) 
        
    
    return next_gen
    
  
next_gen_000 = new_generation(pppp)
next_gen_001 = new_generation(next_gen_000)
    
# successfully implemented 1 generation's evolution.
# now just loop this 100 times or so...
gen_final = next_gen_001
for i in range(100):
    gen_final = new_generation(gen_final)

# WORKS. The final generation individuals all sum up close to 100.

# to test this:

for individual1 in gen_final:
    print(individual1)
    
    
# all the lists have been optimised with the Genetic Algo. to add up to (almost) 100
    
    
