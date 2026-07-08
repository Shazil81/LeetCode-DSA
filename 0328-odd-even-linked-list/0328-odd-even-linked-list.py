# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Optimal solution
        # base condition
        if head is None or head.next is None:
            return head
        odd = head
        even = head.next
        even_head = even
        while even is not None and even.next is not None: # important condition hai
            odd.next = odd.next.next        # odd k address ko change krna
            odd = odd.next
            even.next = even.next.next      # even k address ko change krna
            even = even.next
        odd.next = even_head    # last me odd wale list ko even wale se connect kr do
        return head