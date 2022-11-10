// https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        node = original
        clon = cloned
        stackOrg = []
        stackCloned = []
        
        while node is not None:
            if node.val == target.val:
                if target.val == clon.val:
                    return clon
                
            if node.left is not None:
                print(node.left.val)
                stackOrg.append(node.left)
                stackCloned.append(clon.left)
                
            if node.right is not None:
                print(node.right.val)
                stackOrg.append(node.right)
                stackCloned.append(clon.right)
            node = stackOrg.pop()
            clon = stackCloned.pop()
            
            
        
            