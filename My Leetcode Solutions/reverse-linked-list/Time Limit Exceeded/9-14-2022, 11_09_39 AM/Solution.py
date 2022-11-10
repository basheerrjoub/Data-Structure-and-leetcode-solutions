// https://leetcode.com/problems/reverse-linked-list

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
        rnode = head
        while node != None:
            rnode = node.next
            rnode.next = node
            node = node.next
        return rnode
    
    
        