# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        cnt = 0
        temp = head
        while temp is not None:
            cnt += 1
            temp = temp.next
        # print(cnt)
        k = k % cnt
        if k == 0:
            return head
        z = cnt - k
        temp1 = head
        prev = None
        # print(cnt, z)
        while z > 0:
            prev = temp1
            temp1 = temp1.next
            z -= 1
        ans = temp1
        prev.next = None
        while temp1 is not None and temp1.next is not None:
            temp1 = temp1.next
        temp1.next = head
        return ans
        
