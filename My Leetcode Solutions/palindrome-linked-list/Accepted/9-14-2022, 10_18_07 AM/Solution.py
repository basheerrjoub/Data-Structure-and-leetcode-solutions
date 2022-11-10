// https://leetcode.com/problems/palindrome-linked-list

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        node = head
        strNumber = ""
        while node != None:
            strNumber += str(node.val)
            node = node.next
        revNumberStr = ""
        for i in range(len(strNumber)):
            revNumberStr += strNumber[len(strNumber) - i - 1]
        
        if int(revNumberStr) == int(strNumber):
            return True
        else:
            return False
        