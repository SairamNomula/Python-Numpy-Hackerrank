# Python Floor, Ceil and Rint
# Task
# In this Floor, Ceil, and Rint problem You are given a 1-D array,. Your task is to print the floor, ceil, and rint of all the elements of A.

# Python 3
import numpy

numpy.set_printoptions(sign=' ')

a = numpy.array(input().split(),float)

print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))
