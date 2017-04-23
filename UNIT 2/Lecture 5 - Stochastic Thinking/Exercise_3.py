# Exercise 3

# Exercise 3-1
# 5.0/5.0 points (graded)
# Write a deterministic program, deterministicNumber, that returns an even number between 9 and 21.

# def deterministicNumber():
#     '''
#     Deterministically generates and returns an even number between 9 and 21
#     '''
#     # Your code here


import random
def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    # Your code here
    return 16

# correctCorrect
# Test results
# CORRECT



# Exercise 3-2
# 5.0/5.0 points (graded)
# Write a uniformly distributed stochastic program, stochasticNumber, that returns an even number between 9 and 21.

# def stochasticNumber():
#     '''
#     Stochastically generates and returns a uniformly distributed even number between 9 and 21
#     '''
#     # Your code here


import random
def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    # Your code here
    return random.randrange(10, 21, 2)

# correctCorrect