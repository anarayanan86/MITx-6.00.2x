# Part B: Problem 5
#  Bookmark this page
# Part B: Problem 5: Running and Analyzing a Simulation With a Drug
# 10.0/10.0 points (graded)
# In this problem, we will use the implementation you filled in for Problem 4 to run a simulation. You will create a TreatedPatient
# instance with the following parameters, then run the simulation:
# viruses, a list of 100 ResistantVirus instances
# maxPop, maximum sustainable virus population = 1000

# Each ResistantVirus instance in the viruses list should be initialized with the following parameters:
# maxBirthProb, maximum reproduction probability for a virus particle = 0.1
# clearProb, maximum clearance probability for a virus particle = 0.05
# resistances, The virus's genetic resistance to drugs in the experiment = {'guttagonol': False}
# mutProb, probability of a mutation in a virus particle's offspring = 0.005

# Run a simulation that consists of 150 time steps, followed by the addition of the drug, guttagonol, followed by another 150 time steps.
# You should make use of the function simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials).
# As with problem 3, perform up to 100 trials and make sure that your results are repeatable and representative.

# Create one plot that records both the average total virus population and the average population of guttagonol-resistant virus particles
# over time.

# A few good questions to consider as you look at your plots are: What trends do you observe? Are the trends consistent with your
# intuition? Feel free to discuss the answers to these questions in the forum, to fully cement your understanding of this problem set,
# processing and interpreting data.

# Again, as in Problem 2, you can use the provided .pyc file to check that your implementation of the TreatedPatient and ResistantVirus
# classes work as expected.

# If you want to use numpy arrays, you should import numpy as np and use np.METHOD_NAME in your code.


# Enter your definition for simulationWithDrug in this box
def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """

    # TODO
    import numpy as np
    
    data = np.zeros(300)
    data1 = np.zeros(300)
    for i in range(numTrials):
        virus = ResistantVirus(maxBirthProb, clearProb, resistances, mutProb)
        viruses = [virus] * numViruses
        patient = TreatedPatient(viruses, maxPop)
        virus_count, resist_virus_count = [], []
        for j in range(150):
            patient.update()
            virus_count.append(patient.getTotalPop())
            resist_virus_count.append(patient.getResistPop(['guttagonol']))
        patient.addPrescription('guttagonol')
        for k in range(150):
            patient.update()
            virus_count.append(patient.getTotalPop())
            resist_virus_count.append(patient.getResistPop(['guttagonol']))
        data = data + virus_count
        data1 = data1 + resist_virus_count
    data_avg = data/numTrials
    data1_avg = data1/numTrials
    
    pylab.plot(list([float('{0:.1f}'.format(i)) for i in data_avg]), label = r'Non-resistant population')
    pylab.plot(list([float('{0:.1f}'.format(j)) for j in data1_avg]), label = r'Guttagonol Resistant population')
    pylab.xlabel(r'Number of steps')
    pylab.ylabel(r'Average Virus Population')
    pylab.title(r'Virus Simulation in Patient')
    pylab.legend()
    pylab.show()
    
# Correct
