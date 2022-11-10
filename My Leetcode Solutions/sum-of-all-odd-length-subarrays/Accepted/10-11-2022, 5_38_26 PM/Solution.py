// https://leetcode.com/problems/sum-of-all-odd-length-subarrays

class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        r_sum = sum(arr)
        
        i = 3
        while i <= len(arr):
            k = 0
            j = i
            while j <= len(arr):
                print(sum(arr[k:j]))
                r_sum += sum(arr[k:j])
                j += 1
                k += 1
            i += 2
        return r_sum