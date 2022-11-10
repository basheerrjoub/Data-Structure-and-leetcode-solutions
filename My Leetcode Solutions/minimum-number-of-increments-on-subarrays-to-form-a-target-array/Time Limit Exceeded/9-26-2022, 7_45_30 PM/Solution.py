// https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array

class Solution(object):
    def minNumberOperations(self, target):
        """
        :type target: List[int]
        :rtype: int
        """
        size = len(target)
        ls = [0] * size
        count = 0
        while ls != target:
            count += 1
            for i in range(size):
                if ls[i] == target[i]:
                    continue
                else:
                    if i == (size - 1):
                        ls[i] += 1
                        continue
                    k = i+1
                    while ls[k] == ls[i] and ls[k] != target[k]:
                        ls[k] += 1
                        k += 1
                        if k == size:
                            break
                        
                    ls[i] += 1
                    break
                    
        return count
            