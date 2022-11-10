// https://leetcode.com/problems/intersection-of-two-linked-lists

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        save1 = {}
        save2 = {}
        nodeA, nodeB = headA, headB
        while nodeA is not None:
            save1[nodeA] = 1
            nodeA = nodeA.next
            
        while nodeB is not None:
            if nodeB in save1:
                return nodeB
            nodeB = nodeB.next
        return None