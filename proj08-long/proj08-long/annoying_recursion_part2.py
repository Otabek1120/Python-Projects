""" File: annoying_recursion_part2.py
    Author: Otabek Abduraimov
    Purpose: This python file has three functions
    that use only recursion to solve the problems
    specified in the spec. It uses
    -No loops
    -No helper functions
    -No default arguments
    -Recursion
    Course #: CS 120, Fall 2021
"""


def annoying_triangleNumbers(n):
    """
    :param n: a non-negative integer
    :return: the sum of the numbers till n, including n
    This function calculates the sum of number from 0 to n
    using recursion. It has 4 base cases for n=0,1,2,3 and
    hard-code for n=4,5,6. After that it uses recursion
    to solve the problem
    """
    assert n >= 0
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 3
    elif n == 3:
        return 6
    elif n == 4:
        return 4 + annoying_triangleNumbers(3)
    elif n == 5:
        return 5 + annoying_triangleNumbers(4)
    elif n == 6:
        return 6 + annoying_triangleNumbers(5)
    else:
        return n + annoying_triangleNumbers(n-1)


def annoying_fibonacci_sequence(n):
    """
    :param n: a non-negative integer
    :return: list of n mant fibonacci numbers
    This function creates a list of n many fibonacci numbers
    using recursion. It has 4 base cases for n=0,1,2,3 and
    hard-code for n=4,5,6. After that it uses recursion
    to solve the problem
    """
    assert n >= 0
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    elif n == 3:
        return [0,1,1]
    elif n == 4:
        return annoying_fibonacci_sequence(3) + [2]
    elif n == 5:
        return annoying_fibonacci_sequence(4) + [3]
    elif n == 6:
        return annoying_fibonacci_sequence(5) + [5]
    else:
        return annoying_fibonacci_sequence(n-1) + \
               [sum(annoying_fibonacci_sequence(n-1)[-2:])]
print(annoying_fibonacci_sequence(30))


def annoying_valley(n):
    """
    :param n: a non-negative integer
    :return: None
    This function prints out a valley like shape
    using recursion. It has 4 base cases for n=0,1,2,3 and
    hard-code for n=4,5,6. After that it uses recursion
    to solve the problem
    """
    assert n >= 0
    if n == 0:
        print(end="")
    elif n == 1:
        print("*")
    elif n == 2:
        print("./", "*", ".\\", sep="\n")
    elif n == 3:
        print("../", "./", "*", ".\\", "..\\", sep="\n")
    elif n == 4:
        print(".../")
        annoying_valley(3)
        print("...\\")
    elif n == 5:
        print("..../")
        annoying_valley(4)
        print("....\\")
    elif n == 6:
        print("...../")
        annoying_valley(5)
        print(".....\\")
    else:
        print("." * (n-1) + "/")
        annoying_valley(n-1)
        print("." * (n-1) + "\\")