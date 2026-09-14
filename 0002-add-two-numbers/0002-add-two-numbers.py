# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Optimal one
        dummy = ListNode(0)
        curr = dummy
        carry = 0  # carry concept used

        while l1 or l2 or carry:  # l1 bacha ho ya l2 ya carry tab tk loop run kro
            if l1: # l1 ka value liya
                v1 = l1.val
            else:
                v1 = 0
            if l2: # l2 ka value liya
                v2 = l2.val 
            else:
                v2 = 0
            
            total = v1 + v2 + carry  # total add kiya carry k sath

            carry = total // 10  # carry nikalne ka concept

            curr.next = ListNode(total % 10)  # last digit nikala or uska node bna diya

            # Pointers Updating
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            
        return dummy.next