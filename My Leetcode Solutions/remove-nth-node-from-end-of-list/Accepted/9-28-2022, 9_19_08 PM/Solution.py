// https://leetcode.com/problems/remove-nth-node-from-end-of-list

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        node = head 
        newNode = None
        prev = None
        
        while node: 
          nex = node.next
          newNode = node
          newNode.next = prev
          prev = node
          node = nex
        
        if n == 1:
            newNode = newNode.next
        temp = newNode
        
        node = temp 
        newNode = None
        prev = None
        count = 1
        while node:
          if count == n-1:
            node.next = node.next.next
            
          count +=1
          nex = node.next
          newNode = node
          newNode.next = prev
          prev = node
          node = nex
                
            
            
        
        return newNode
        
        
                