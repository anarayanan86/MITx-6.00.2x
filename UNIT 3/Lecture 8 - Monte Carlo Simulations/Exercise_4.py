# Exercise 4

# Exercise 4
# 5.0/5.0 points (graded)
# You have a bucket with 3 red balls and 3 green balls. Assume that once you draw a ball out of the bucket, you don't replace it. What is
# the probability of drawing 3 balls of the same color?

# Write a Monte Carlo simulation to solve the above problem. Feel free to write a helper function if you wish.


def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
    if numTrials >= 1:
        results = []
        for i in range(numTrials):
            bucket = ['R', 'R', 'R', 'G', 'G', 'G']
            draws = []
            for j in range(3):
                choice = random.choice(bucket)
                draws.append(choice)
                bucket.remove(choice)
            results.append(draws)
        counter = 0
        for k in results:
            if k[0] == k[1] == k[2]:
                counter += 1
        return counter/float(numTrials)           
    else:
        return 'numTrials must be greater than 0'      
        
# correctCorrect
