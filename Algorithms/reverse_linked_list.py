# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        prev = None
        if not node or not node.next:
            return node
        while node:
            current = node
            next = node.next
            node.next = prev
            prev = current
            node = next
        return current
    
    
        