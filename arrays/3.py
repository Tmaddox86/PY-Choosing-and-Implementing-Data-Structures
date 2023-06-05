# Use a single operation (no loops) to multiply every element of an array by 3.

import numpy as np
a = np.array([1,2,3,4,5])

#arr = [1, 2, 3, 4, 5]
#arr = [i * 3 for i in arr]
#print(arr)



def multiply_elements_by_3(arr):
    return 3 * arr

multiply_elements_by_3(a)