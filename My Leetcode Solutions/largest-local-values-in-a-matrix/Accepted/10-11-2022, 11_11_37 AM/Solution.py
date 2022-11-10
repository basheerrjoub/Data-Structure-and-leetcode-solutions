// https://leetcode.com/problems/largest-local-values-in-a-matrix

class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        grid_len = len(grid)-2
        sub_len = len(grid[0])-2
        i  = j = 0
        r_list = []
        while i < grid_len:
            r_list.append([])
            j=0
            while j < sub_len:
                r_list[i].append(max(grid[i][j:j+3] + grid[i+1][j:j+3] + grid[i+2][j:j+3]))
                j+=1
            
            i+=1
        return r_list