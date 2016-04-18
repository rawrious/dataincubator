import random
from array import *

import numpy as np

# Variables
N = 2  # specified by DI
T = random.sample(range(10), 8)  # create k random numbers, where k is specified by DI
a = 32  # conditional probability, floor
b = 64  # conditional probability, ceiling

# Registers
for i in T:

    Last = array('i')  # holds the last N numbers encountered
    if len(Last) > N:
        Last.remove([0])

    Max = array('i')  # holds the largest numbers encountered
    for k in Last:
        if Last.array([i]) > Max:
            max = Last.array.append([i])

# M is the product of the numbers in the 'max' register
M = np.prod(Max)
print(M)

# L is the product of the numbers in teh 'last' register
L = np.prod(Last)
print(L)

# # M-L Calcs
# # this needs to be an array of <1000 dudes
# sub = array('i')
# dudette = array('i')
#
# for i in range(1000):
#     sub = np.subtract(M, L)
#     dude = array.append(dudette)
#
# print("dude equals " + dude)
#
# mean = np.mean(dude)
# std = np.std(dude)
#
# print("the mean is " + mean)
# print("the std dev is " + std)
#
# # conditional probabilities
