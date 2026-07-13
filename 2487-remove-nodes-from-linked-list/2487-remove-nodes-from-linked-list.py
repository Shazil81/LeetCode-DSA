# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Without Stack is optimal one
        # 1. Reverse the list
        prev = None
        curr = head
        while curr:
            front = curr.next
            curr.next = prev
            prev = curr
            curr = front
        
        # 2. Traverse and remove nodes smaller than max_val
        reversed_head = prev
        max_val = -1
        dummy = ListNode(0)
        tail = dummy
        
        curr = reversed_head
        while curr:
            if curr.val >= max_val:
                max_val = curr.val
                # Add to our result list
                tail.next = curr
                tail = tail.next
            curr = curr.next
            
        # 3. Terminate and reverse back to original order
        tail.next = None
        
        # Final reverse to fix order
        prev = None
        curr = dummy.next
        while curr:
            front = curr.next
            curr.next = prev
            prev = curr
            curr = front
            
        return prev

