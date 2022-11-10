// https://leetcode.com/problems/add-two-numbers

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node1 = l1
        node2 = l2
        sum1 = 0
        sum2 = 0
        i = 1
        while node1 is not None or node2 is not None:
            if node1 is not None:
                sum1 += node1.val * i
                node1 = node1.next
            if node2 is not None:
                sum2 += node2.val * i
                node2 = node2.next
            
            
            i = i*10
        sum = sum1 + sum2
        
        number = sum % 10
        sum = sum / 10
        sumNode = ListNode(number)
        rList = sumNode
        while sum != 0:
            number = sum % 10
            sum = sum /10
            sumNode.next = ListNode(number)
            sumNode = sumNode.next
        return rList
            
            
            
            
            