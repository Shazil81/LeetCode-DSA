# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Optimal Solution two pointer approach
        
        slow = head
        fast = head
        for _ in range(n): # jitna n wha pe pehle hi fast ko rkh denge
            fast = fast.next
        # Special case
        if fast is None:
            return head.next
            
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head