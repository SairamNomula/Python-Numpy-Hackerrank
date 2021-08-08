# Python Zeros and ones
# Task
# You are given the shape of the array in the form of space-separated integers, each integer representing the size of different dimensions, your task is to print an array of the given shape and integer type using the tools numpy.zeros and numpy.ones.
# Input Format
# A single line containing the space-separated integers.
# Constraints
# 1 <= each integer <= 3


# Language : python 3
import numpy

size = tuple(map(int,input().strip().split()))
print(numpy.zeros(size, int))
print(numpy.ones(size, int))
