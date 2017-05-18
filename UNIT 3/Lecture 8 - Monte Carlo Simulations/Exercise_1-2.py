# Exercise 1-2
# 5.0/5.0 points (graded)
# We are handed a biased coin and want to infer the probability that it lands on heads. Use the code provided for CLT, along with the
# provided helper function flipCoin, to generate confidence intervals for the probability of heads. You should only need to change a few
# lines of code.

# You have two files: flipcoin.py with the code to fill in and with some code to plot the results, and coin_flips.txt with the flip data.

####################
## Helper functions#
####################
def flipCoin(numFlips):
    '''
    Returns the result of numFlips coin flips of a biased coin.

    numFlips (int): the number of times to flip the coin.

    returns: a list of length numFlips, where values are either 1 or 0,
    with 1 indicating Heads and 0 indicating Tails.
    '''
    with open('coin_flips.txt','r') as f:
        all_flips = f.read()
    flips = random.sample(all_flips, numFlips)
    return [int(flip == 'H') for flip in flips]


def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

    
#############################
## CLT Hands-on             #
##                          #
## Fill in the missing code #
## Do not use numpy/pylab   #
#############################
meanOfMeans, stdOfMeans = [], []
sampleSizes = range(10, 500, 50)

def clt():
    """ Flips a coin to generate a sample. 
        Modifies meanOfMeans and stdOfMeans defined before the function
        to get the means and stddevs based on the sample means. 
        Does not return anything """
    for sampleSize in sampleSizes:
        sampleMeans = []
        for t in range(20):
            sample = ## FILL THIS IN
            sampleMeans.append(getMeanAndStd(sample)[0])
        ## FILL IN TWO LINES
        ## WHAT TO DO WITH THE SAMPLE MEANS?
  
# Paste only the clt() function.

None
def clt():
    """ Flips a coin to generate a sample. 
        Modifies meanOfMeans and stdOfMeans defined before the function
        to get the means and stddevs based on the sample means. 
        Does not return anything """
    for sampleSize in sampleSizes:
        sampleMeans = []
        for t in range(20):
            sample = flipCoin(sampleSize) ## FILL THIS IN
            sampleMeans.append(getMeanAndStd(sample)[0])
        ## FILL IN TWO LINES
        ## WHAT TO DO WITH THE SAMPLE MEANS?
        meanOfMeans.append(getMeanAndStd(sampleMeans)[0])
        stdOfMeans.append(getMeanAndStd(sampleMeans)[1])


# correctCorrect
