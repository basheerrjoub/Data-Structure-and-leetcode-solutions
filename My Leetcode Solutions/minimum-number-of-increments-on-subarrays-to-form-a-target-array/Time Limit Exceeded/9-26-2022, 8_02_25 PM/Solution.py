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
                if ls[i] != target[i]:
                    for j in range(i + 1, size):
                        if ls[i] == ls[j] and ls[j] != target[j]:
                            ls[j] += 1
                        else:
                            break
                    ls[i] += 1
                    break

                    
        return count
            