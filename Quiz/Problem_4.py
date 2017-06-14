# Problem 4
#  Bookmark this page
# Problem 4
# 15.0/15.0 points (graded)
# You are given a list of unique positive integers L sorted in descending order and a positive integer sum s. The list has n elements.
# Consider writing a program that finds values for multipliers m0,m1,...,mn−1 such that the following equation holds:
# s=L[0]∗m0+L[1]∗m1+...+L[n−1]∗mn−1
# Assume a greedy approach to this problem. You calculate the integer multipliers m_0, m_1, ..., m_(n-1) by finding the largest
# multiplier possible for the largest value in the list, then for the second largest, and so on. Write a function that returns the sum
# of the multipliers using this greedy approach. If the greedy approach does not yield a set of multipliers such that the equation above
# sums to s, return the string "no solution". Write the function implementing this greedy algorithm with the specification below:

# def greedySum(L, s):
#     """ input: s, positive integer, what the sum should add up to
#                L, list of unique positive integers sorted in descending order
#         Use the greedy approach where you find the largest multiplier for 
#         the largest value in L then for the second largest, and so on to 
#         solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
#         return: the sum of the multipliers or "no solution" if greedy approach does 
#                 not yield a set of multipliers such that the equation sums to 's'
#     """


def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """
    multipliers = []
    remain = s
    for i in L:
        if i <= remain:
            mult = remain // i
            multipliers.append(mult)
            remain -= i * mult
        else:
            multipliers.append(0)
    sum1 = 0
    for j in range(len(multipliers)):
        sum1 += L[j]*multipliers[j]
    if sum1 == s:
        return sum(multipliers)
    else:
        return 'no solution'
        
correctCorrect
