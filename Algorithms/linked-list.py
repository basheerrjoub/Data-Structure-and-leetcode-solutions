class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


n1 = ListNode(1)
n2 = ListNode(2); n1.next = n2
n3 = ListNode(3); n2.next = n3
n4 = ListNode(4); n3.next = n4
n5 = ListNode(5); n4.next = n5
n6 = ListNode(6); n5.next = n6

node = n1
dummy = ListNode()
while node:
    dummy.next = node
    dummy = dummy.next
    node = node.next
print (dummy.val)