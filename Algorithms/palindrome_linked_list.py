# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def isPalindrome(head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        node = head
        strNumber = ""
        while node != None:
            strNumber += str(node.val)
            node = node.next
        length = len(strNumber)
        if length == 1 or (length == 2 and strNumber[0] == strNumber[1]):
            return True

        even = False
        if length % 2 == 0:
            even = True

        half = (len(strNumber) // 2) 
        
        leftI = half -1
        rightI = half +1
        if even:
            while strNumber[leftI] == strNumber[rightI - 1]  and leftI >=0 and rightI-1 < length:
                if leftI == 0:
                    return True
                leftI -= 1
                rightI +=1
        if not even:
            while strNumber[leftI] == strNumber[rightI]  and leftI >=0 and rightI < length:
                if leftI == 0:
                    return True
                leftI -= 1
                rightI +=1
        return False
# 1 1 1 1

    node1 = ListNode(2)
    node2 = ListNode(1); node1.next = node2
    node3 = ListNode(2); node2.next = node3
    node4 = ListNode(1); node3.next = node4
    node5 = ListNode(2); node4.next = node5

    
    
    print(isPalindrome(node1))