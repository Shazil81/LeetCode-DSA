# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # optimal one
        # 1. Find midpoint
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # 2. Reverse second half
        prev = None
        curr = slow
        while curr:
            front = curr.next
            curr.next = prev
            prev = curr
            curr = front
            
        # 3. Calculate Max Twin Sum
        maxi = 0
        first_half = head
        second_half = prev # 'prev' is the head of reversed list
        
        while second_half:
            maxi = max(maxi, first_half.val + second_half.val)
            first_half = first_half.next
            second_half = second_half.next
            
        return maxi
