// https://leetcode.com/problems/same-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        stack1 = []; stack1.append(p)
        stack2 = []; stack2.append(q)
        
        while len(stack1) and len(stack2):
            node1 = stack1.pop(0)
            node2 = stack2.pop(0)
            if (not node1 and  node2) or (node1 and  not node2):
                return False 
            elif not node1 and not node2:
                continue
            elif node1.val != node2.val:
                return False
            stack1.append(node1.left)
            stack1.append(node1.right)
            stack2.append(node2.left)
            stack2.append(node2.right)
        return True