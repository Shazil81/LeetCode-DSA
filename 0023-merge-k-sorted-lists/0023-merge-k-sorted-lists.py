# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # heap k sath kr rhe hain
        # step 1 sare values ko ek list me daal dete hain
        heap = []
        for node in lists:
            while node:
                heapq.heappush(heap, node.val)
                node = node.next
        # step 2 heap se pop krte jao or naya linked list bnao kyun ki minimum wala hi pop hoga baar baar
        dummy = ListNode(0)
        curr = dummy
        
        while heap:
            curr.next = ListNode(heapq.heappop(heap))
            curr = curr.next
        return dummy.next
        