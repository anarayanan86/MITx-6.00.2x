# Generating a Power Set
# This assignment has several steps. In the first step, you'll provide a response to the question. The other steps appear 
# below the Your Response field.

# Your Response
# due Dec 31, 2028 16:00 PST (in 11 years, 9 months)
# IN PROGRESS
# Enter your response to the question. You can save your progress and return to complete your response at any time before
# the due date (Sunday, Dec 31, 2028 16:00 PST). After you submit your response, you cannot edit it.

# The prompt for this section
# (this exercise is not graded)

# One of the joys of Python is that there are many clever ways of implementing most algorithms. Another joy is that Python
# has a large following of programmers, and often these programmers post their most elegant "recipes" on the web. So when
# you need an implementation for a tricky algorithm, a good first step is to search for an existing solution you might be
# able to use or adapt (except for on your problem sets when you're supposed to be learning!

# Do a web search for "python power set" to locate other elegant Python recipes for generating the power set for a list of
# items. In particular, look for solutions that use the itertools module. The itertools module is an extremely useful
# toolkit, particularly for optimization problems. The code graders in 6.00.1x/2x that grade your code submissions make
# frequent use of this module!

# YOUR TASK
# Your task is to now rewrite the powerSet(items) generator from the previous problem to make use of these recipes. Perform
# a test run. The runtime may not be noticeably different, but shorter, more elegant code is often a good investment,
# particularly if other programmers will be responsible for its upkeep in the future.

# Attach your solutions below to send them to another student to look at. If you do this, you will get to see someone else's
# solution!

# *** Attach a .py file. In the text box, enter anything, like "attached". ***

from itertools import chain, combinations

def powerSet(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))