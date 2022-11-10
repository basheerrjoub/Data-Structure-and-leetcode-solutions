def findMedianSortedArrays(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        if len1 > len2:
            len1, len2 = len2, len1
            nums1, nums2 = nums2, nums1
        
        half = (len1 + len2) // 2
        
        med1 = (len1 // 2)
        med2 = half - med1
        med1 -= 1
        med2 -= 1
        while nums1[med1] > nums2[med2+1] or nums2[med2] > nums1[med1+1]:
            if nums1[med1] > nums2[med2+1]:
                med1 -=1
                med2 +=1
                if med1 == -1:
                    break
            if nums2[med2] > nums1[med1+1]:
                med1 +=1
                med2 -=1
                if med2 == -1:
                    break
        
        maxLeft = max(nums1[med1], nums2[med2])
        minRight = min(nums1[med1+1], nums2[med2+1])
        
        return  (maxLeft + minRight) / 2
        
            
# 1 2        3   4
# 1 2 3 4    5 6 7 8

# 1 2 3      4
# 1 2 3      4 5 6 7 8    
print(findMedianSortedArrays([1,2], [3,4]))