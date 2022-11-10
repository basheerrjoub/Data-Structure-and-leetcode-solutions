// https://leetcode.com/problems/deepest-leaves-sum

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        
        self.maxLevel = 0
        self.sumLeaves = 0
        def dfs(root, level):
            level +=1
            if not root:
                return
            if level > self.maxLevel:
                self.maxLevel = level
                self.sumLeaves = root.val
            elif level == self.maxLevel:
                self.sumLeaves += root.val             
            
            
            dfs(root.left, level)
            dfs(root.right, level)
        dfs(root, 0)
        return self.sumLeaves
            
            
            
        
        