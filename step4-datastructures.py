import time

def datastructuresearch(subset, universal):
    """Get intersection of two lists with set().intersection() method
set(list1).intersection(list2) returns a list which is an intersection of the two lists.
The length of the list gives the number of elements in list1 common with list2
"""
    start = time.time()
    print(len(set(subset_elements).intersection(all_elements)))
    print('Duration: {} seconds'.format(time.time() - start))

with open('subset_elemets.txt') as f:
    subset_elements = f.read().split('\n')
    
with open('all_elements.txt') as f:
    all_elements = f.read().split('\n')

print(datastructuresearch.__doc__)
datastructuresearch(subset_elements, all_elements)


