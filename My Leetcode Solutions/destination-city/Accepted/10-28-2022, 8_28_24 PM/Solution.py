// https://leetcode.com/problems/destination-city

class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        dic = {}
        for path in paths:
            dic[path[0]] = path[1]
        
        for path in paths:
            if path[1]  not in dic:
                return path[1]