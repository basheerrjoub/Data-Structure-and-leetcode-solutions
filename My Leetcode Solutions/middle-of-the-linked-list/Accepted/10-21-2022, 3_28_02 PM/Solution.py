// https://leetcode.com/problems/middle-of-the-linked-list

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        vals = {}
        i = 0
        if not node:
            return head
        if node.next is None:
            return head
        while node is not None:
            i+=1
            vals[i] = node
            node = node.next

        
        return vals[i//2].next
            