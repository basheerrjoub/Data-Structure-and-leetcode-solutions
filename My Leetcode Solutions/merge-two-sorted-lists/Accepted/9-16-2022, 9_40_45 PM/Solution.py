// https://leetcode.com/problems/merge-two-sorted-lists

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        rList = ListNode()
        head = rList
        while list1 and list2:
            if list1.val < list2.val:
                rList.next = list1
                list1 = list1.next
            else:
                rList.next = list2
                list2 = list2.next
            rList = rList.next
        while list1:
            rList.next = list1
            list1 = list1.next
            rList = rList.next
            
        while list2:
            rList.next = list2
            list2 = list2.next
            rList = rList.next
        
        return head.next
            
        