# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap=[]
        heapq.heapify(heap)
        for i in range(len(lists)):
            if lists[i] is not None:
                heapq.heappush(heap,[lists[i].val,i])
                lists[i]=lists[i].next
        root=None
        while heap:
            curr=heapq.heappop(heap)
            if lists[curr[1]] is not None:
                heapq.heappush(heap,[lists[curr[1]].val,curr[1]])
                lists[curr[1]]=lists[curr[1]].next
            if root==None:
                root=ListNode(curr[0])
                temp=root
            else:
                temp.next=ListNode(curr[0])
                temp=temp.next
        return root