// https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        node = head
        number = ""
        while node is not None:
            number += str(node.val)
            node = node.next
        return int(number, 2)