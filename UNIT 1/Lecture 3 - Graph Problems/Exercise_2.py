# Exercise 2

# Exercise 2
# 10/10 points (graded)
# Consider our representation of permutations of students in a line from Exercise 1. (The teacher only swaps the positions of two
# students that are next to each other in line.) Let's consider a line of three students, Alice, Bob, and Carol (denoted A, B, and C).
# Using the Graph class created in the lecture, we can create a graph with the design chosen in Exercise 1: vertices represent
# permutations of the students in line; edges connect two permutations if one can be made into the other by swapping two adjacent
# students.

# We construct our graph by first adding the following nodes:

nodes = []
nodes.append(Node("ABC")) # nodes[0]
nodes.append(Node("ACB")) # nodes[1]
nodes.append(Node("BAC")) # nodes[2]
nodes.append(Node("BCA")) # nodes[3]
nodes.append(Node("CAB")) # nodes[4]
nodes.append(Node("CBA")) # nodes[5]

g = Graph()
for n in nodes:
    g.addNode(n)
# Add the appropriate edges to the graph.

# Hint: How to get started?
# Write your code in terms of the nodes list from the code above. For each node, think about what permutation is allowed. A permutation
# of a set is a rearrangement of the elements in that set. In this problem, you are only adding edges between nodes whose permutations
# are between elements in the set beside each other. For example, an acceptable permutation (edge) is between "ABC" and "ACB" but not
# between "ABC" and "CAB".


# Write the code that adds the appropriate edges to the graph
# in this box.
g.addEdge(Edge(nodes[0], nodes[1]))
g.addEdge(Edge(nodes[0], nodes[2]))
g.addEdge(Edge(nodes[1], nodes[4]))
g.addEdge(Edge(nodes[2], nodes[3]))
g.addEdge(Edge(nodes[3], nodes[5]))
g.addEdge(Edge(nodes[4], nodes[5]))


# correctCorrect
