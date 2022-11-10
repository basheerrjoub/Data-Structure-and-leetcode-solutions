// https://leetcode.com/problems/decode-xored-array

class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        r_list = [first]
        
        length = len(encoded)
        i = 0
        while i < length:
            r_list.append(r_list[i] ^ encoded[i])
            i += 1
        return r_list