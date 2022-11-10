############################################
#                                          #
#                quick sort                #
#           Worst case = O(n^2)            #
#         Average case = O(nlogn)          #
#                                          #
############################################

from math import floor

#Quicksort with the best case pivot = half of the array
def quickSortBC(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[floor(len(array)/2)]
        greater = [i for i in array[1:] if i >= pivot]
        less = [i for i in array[1:] if i < pivot]
        return quickSortBC(less) + [pivot] + quickSortBC(greater)



#Quicksort with the worst case pivot = first item of array
def quickSortWC(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        greater = [i for i in array[1:] if i >= pivot]
        less = [i for i in array[1:] if i < pivot]
        return quickSortWC(less) + [pivot] + quickSortWC(greater)

array = [180,165,170]
sorted_array = quickSortBC(array)
print (sorted_array)
    