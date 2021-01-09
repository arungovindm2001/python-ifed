import time
import numpy as np

def numpysearch(subset, universal):
    """Search elements faster with numpy
np.in1d(list1,list2) returns a list with boolean values True and False.
True if the element in list1 is present in list2, and False if there isn't.
The True elements are appended to a list called verified.
The length of the list gives the number of elements present in list2 which is common with list1.
"""
    start = time.time()
    verified = []
    for boolvalue in np.in1d(subset,universal):
        if boolvalue:
            verified.append(boolvalue)
    print(len(verified))
    print('Duration: {} seconds'.format(time.time() - start))

with open('subset_elemets.txt') as f:
    subset_elements = f.read().split('\n')
    
with open('all_elements.txt') as f:
    all_elements = f.read().split('\n')

print(numpysearch.__doc__)
numpysearch(subset_elements, all_elements)
    

