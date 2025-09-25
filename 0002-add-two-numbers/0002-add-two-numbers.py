# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        root=None
        carry=0
        while l1 is not None or l2 is not None :
            z=carry
            if l1 is not None:
                z+=l1.val
                l1=l1.next
            if l2 is not None:
                z+=l2.val
                l2=l2.next
            nn=ListNode(z%10)
            carry=z//10
            if root is None:
                root=nn
                temp=root
            else:
                temp.next=nn
                temp=temp.next
        if carry>0:
            temp.next=ListNode(carry)
        return root

        