# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        lst.sort()
        ans = ListNode(lst[0])
        temp = ans
        for i in lst[1::]:
            ans.next = ListNode(i)
            ans = ans.next
        return temp