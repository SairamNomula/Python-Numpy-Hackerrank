# Python Sum and Prod
# Task 
# You are given a 2-D array with dimensions NXM.
# Your task is to perform the sum tool over axis 0 and then find the product of that result.

import numpy

N_M = map(int, raw_input().split())
a = numpy.array([map(int, raw_input().split()) for i in range(N_M[0])])
print numpy.prod(numpy.sum(a, axis = 0 ))
