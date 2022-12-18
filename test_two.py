"""
Write a function that takes as arguments two arrays of integers. 
Your function needs to determine whether the second array is contained in the first one, returning true or false;
"""

import numpy as np

def contains_second_array(array_one, array_two):
        # Write your code here
        a = np.array(array_one)
        b = np.array(array_two)
        contains_a_b = np.isin(array_one, array_two)
        print(contains_a_b)
        pass



if __name__=="__main__":

        array_one = [5, 1, 22, 25, 6, -1, 8, 10]
        array_two = [1, 6, -1, 10]

        contains_second_array(array_one, array_two)

