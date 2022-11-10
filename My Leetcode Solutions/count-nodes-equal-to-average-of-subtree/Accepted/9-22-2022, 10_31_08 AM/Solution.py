// https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfSubtree(self, root):
        
        self.numOfNodes = 0
        def dfs(node):

            if not node:
                return 0, 0
            
            sumLeft, countLeft = dfs(node.left)
            sumRight, countRight = dfs(node.right)
            curSum = sumLeft + sumRight + node.val
            curCount = countLeft + countRight + 1
            if  (curSum // curCount) == node.val:
                self.numOfNodes +=1
                
            return curSum, curCount
        
        dfs(root)
        return self.numOfNodes
            
        