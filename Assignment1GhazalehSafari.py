#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 17:47:18 2021

@author: Ghazaleh Safari

International Master- and PhD program in Mathematics
"""

# =============================================================================
#  import modules
# =============================================================================
import numpy as np
import matplotlib.pyplot as plt 


# =============================================================================
# #defining a function to generate random walk for making randomly some data 
# =============================================================================

"""Function for generating a discrete random walk with increments -1 and 1 with
specified length. 
    parameters
    -----------
    length: int
        Length
        
    returns
    --------
    
random_walk_realization: array of int random walk of length """

def generate_random_walk(length):
    sample=np.random.choice([-1, 1], size=length)
    random_walk_realization= np.cumsum(sample)
    return random_walk_realization


# =============================================================================
# Generate some data and plot them
# =============================================================================
"""plotting x axis by generating some data labeled "Time" """

x_values= np.arange(0, 10, 0.1)
plt.xlabel("Time")

"""making an empty list named "a", and writting a for_loop to make
y_values. the firm wants to invest on 20 assetes in the same price. 
so the y_random_walk for eache one at the 0 moment is 1000. makin 99 other 
members of random walks (overal 100 days) by using the func "generate_random_walk"
and adding to the list named y_random_walk. because of that for_loop is local
we add these members to our empty list named "a". changing the list
y_random_walk to an array. finally, printing and ploting 20 investments 
by blue lines
(taskes 1 & 2)  
"""
a=[]
for i in range (20):
    y_random_walk= [1000]
    y_random_walk.extend (1000 + generate_random_walk(99))
    a.append(y_random_walk)
    y_random_walk=np.array(y_random_walk)
    print(f"asset {i}= {y_random_walk}\n")

    plt.plot(x_values,y_random_walk, "b")
plt.ylabel("Assets")  

"""
(task 3) changing list named "a" to a matrix and using sum method to sum the 
columns of the matrix and taking average of them by deviding on 20. printting 
them and ploting on the same figure as red line
"""
a= np.array(a)
average_time_series= a.sum(axis=0)/20
print(f"average time series: {average_time_series}")

plt.plot(x_values, average_time_series, "r")

plt.show()
