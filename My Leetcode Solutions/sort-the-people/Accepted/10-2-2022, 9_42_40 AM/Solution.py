// https://leetcode.com/problems/sort-the-people

class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        def quickSortBC(array):
            if len(array) < 2:
                return array
            else:
                pivot = array[0]
                greater = [i for i in array[1:] if i > pivot]
                less = [i for i in array[1:] if i <= pivot]
                return quickSortBC(greater) + [pivot] + quickSortBC(less)
        save = {}
        for i in range(len(heights)):
            save[heights[i]] = names[i]
        
        heights = quickSortBC(heights)
        
        newList = []
        for h in heights:
            newList.append(save[h])
            
        return newList