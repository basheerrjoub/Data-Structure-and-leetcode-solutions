class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        if len(nums1) == 0:
            return nums1
        i = 0
        
        while i < len(nums1):
            if nums1[i] not in nums2:
                nums1.remove(nums1[i])
                i -= 1
            else:
                nums2.remove(nums1[i])
            i+=1
        return nums1
        