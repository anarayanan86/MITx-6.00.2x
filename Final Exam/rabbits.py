import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    # TO DO
    #pass
    for i in range(CURRENTRABBITPOP):
        if random.random() <= (1 - (CURRENTRABBITPOP/MAXRABBITPOP)):
            CURRENTRABBITPOP += 1
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    # TO DO
    #pass
    for i in range(CURRENTFOXPOP):
        if CURRENTRABBITPOP > 10:
            if random.random() <= (CURRENTRABBITPOP/MAXRABBITPOP):
                CURRENTRABBITPOP -= 1
                # fox reproducing
                if random.random() <= (1/3):
                    CURRENTFOXPOP += 1
        else:
            # fox dying
            if random.random() <= 0.9:
                CURRENTFOXPOP -= 1
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    # TO DO
    #pass
    rabbits = []
    foxes = []
    for i in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbits.append(CURRENTRABBITPOP)
        foxes.append(CURRENTFOXPOP)
    return rabbits, foxes

print(runSimulation(200))

# Plotting for Problem 8 Part B
def plotSimulation(numSteps):
    rabbits = []
    foxes = []
    for i in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbits.append(CURRENTRABBITPOP)
        foxes.append(CURRENTFOXPOP)
    pylab.plot(range(numSteps), rabbits, label = 'rabbits')
    rabbit_coeff = pylab.polyfit(range(numSteps), rabbits, 2)
    pylab.plot(pylab.polyval(rabbit_coeff, range(numSteps)))
    pylab.plot(range(numSteps), foxes, label = 'foxes')
    fox_coeff = pylab.polyfit(range(numSteps), foxes, 2)
    pylab.plot(pylab.polyval(fox_coeff, range(numSteps)))
    pylab.show()
    
plotSimulation(200)