# Problem 4: Running the Simulation

# Problem 4: Running the Simulation
# 10.0/10.0 points (graded)
# In this problem you will write code that runs a complete robot simulation.

# Recall that in each trial, the objective is to determine how many time-steps are on average needed before a specified fraction of the
# room has been cleaned. Implement the following function:

# def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
#                   robot_type):
#     """
#     Runs NUM_TRIALS trials of the simulation and returns the mean number of
#     time-steps needed to clean the fraction MIN_COVERAGE of the room.
#
#     The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
#     speed SPEED, in a room of dimensions WIDTH x HEIGHT.
#     """
# The first six parameters should be self-explanatory. For the time being, you should pass in StandardRobot for the robot_type parameter,
# like so:

# avg = runSimulation(10, 1.0, 15, 20, 0.8, 30, StandardRobot)
# Then, in runSimulation you should use robot_type(...) instead of StandardRobot(...) whenever you wish to instantiate a robot. (This
# will allow us to easily adapt the simulation to run with different robot implementations, which you'll encounter in Problem 6.)

# Feel free to write whatever helper functions you wish.

# We have provided the getNewPosition method of Position, which you may find helpful:

# class Position(object):
#
#     def getNewPosition(self, angle, speed):
#         """
#         Computes and returns the new Position after a single clock-tick has
#         passed, with this object as the current position, and with the
#         specified angle and speed.
#
#         Does NOT test whether the returned position fits inside the room.
#
#         angle: integer representing angle in degrees, 0 <= angle < 360
#         speed: positive float representing speed
#
#         Returns: a Position object representing the new position.
#         """
# For your reference, here are some approximate room cleaning times. These times are with a robot speed of 1.0.
# One robot takes around 150 clock ticks to completely clean a 5x5 room.
# One robot takes around 190 clock ticks to clean 75% of a 10x10 room.
# One robot takes around 310 clock ticks to clean 90% of a 10x10 room.
# One robot takes around 3322 clock ticks to completely clean a 20x20 room.
# Three robots take around 1105 clock ticks to completely clean a 20x20 room.
# (These are only intended as guidelines. Depending on the exact details of your implementation, you may get times slightly different
# from ours.)

# You should also check your simulation's output for speeds other than 1.0. One way to do this is to take the above test cases, change
# the speeds, and make sure the results are sensible.

# For further testing, see the next page in this problem set about the optional way to use visualization methods. Visualization will help
# you see what's going on in the simulation and may assist you in debugging your code.

# Enter your code for the definition of runSimulation below.


# Enter your code for runSimulation in this box.
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """
    #raise NotImplementedError
    # do this in a while loop, but has to be in for loop of num_trials:
    # and instantiate a container to store the results
    results = []
    for i in range(num_trials):
        #anim = ps2_visualize.RobotVisualization(num_robots, width, height)
        num_steps = 0
        # Instantiate a new room
        room = RectangularRoom(width, height)
        # Instantiate the robots
        robots = [robot_type(room, speed) for j in range(num_robots)]
        while (room.getNumCleanedTiles()/room.getNumTiles()) < min_coverage:
            num_steps += 1
            #anim.update(room, robots)
            for k in robots:
                k.updatePositionAndClean()
            if (room.getNumCleanedTiles()/room.getNumTiles()) >= min_coverage:
                results.append(num_steps)
                #anim.done()
            else:
                continue
    # return mean
    return sum(results)/len(results)
    
    
correctCorrect
