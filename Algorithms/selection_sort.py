##################Selection Sort############################
# Sorting by finding the the desired biggest or smallest   #
#number at each iteration until completing the whole list  #
# O(n n-1 n-2 n-3...) = O(n^2)                             #
############################################################
import time
start_time = time.time()

#Data to be sorted
names = ['Jamil', 'Marin', 'Rileigh', 'Izaak', 'Idris', 'Lanie', 'Paisley',
 'Jacobo', 'Aayden', 'Yasmine', 'Yitzchok', 'Petra', 'Jaslyn', 'Samira',
  'Leona', 'Jordan', 'Anna', 'Yeshua', 'Elliott', 'Lesley', 'Jaceyon', 'Javier',
 'Terry', 'Jancarlos', 'Akeem', 'Ethan', 'Keyla', 'Demetrius', 'Mallory', 'Greta']


def smallestNumber(array): 
    element = array[0]
    index = 0
    for i in range(1, len(array)):
        if element > array[i]:
            element = array[i]
            index = i
    
    return index

def Selection_Sort(array):
    newArray = []
    for i in range(len(array)):
        smallest_number = smallestNumber(array)
        newArray.append(array.pop(smallest_number))
    return newArray


print(Selection_Sort(names))
print("This  took " + str(time.time() - start_time) + " seconds")