# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # sorting ka use kr k krenge
        # step 1 sare values ko ek list me daal dete hain
        values = []
        for node in lists:
            while node:
                values.append(node.val)
                node = node.next
        # step 2 sort kr do or nya linked list bna do or daal
        values.sort()
        dummy = ListNode(0)
        curr = dummy
        
        for val in values:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next
        