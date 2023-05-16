# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        sum_head = tmp_head = ListNode()
        
        carry = 0
        while l1 and l2:
            curr_sum = l1.val + l2.val + carry
            if curr_sum >= 10:
                carry = curr_sum // 10
                curr_sum %= 10
            else:
                carry = 0
            tmp_head.next = ListNode(curr_sum)
            tmp_head = tmp_head.next
            l1 = l1.next
            l2 = l2.next
            
        while l1:
            curr_sum = l1.val + carry
            if curr_sum >= 10:
                carry = curr_sum // 10
                curr_sum %= 10
            else:
                carry = 0
            tmp_head.next = ListNode(curr_sum)
            tmp_head = tmp_head.next
            l1 = l1.next
        
        while l2:
            curr_sum = l2.val + carry
            if curr_sum >= 10:
                carry = curr_sum // 10
                curr_sum %= 10
            else:
                carry = 0
            tmp_head.next = ListNode(curr_sum)
            tmp_head = tmp_head.next
            l2 = l2.next
        
        if carry:
            tmp_head.next = ListNode(carry)
            
        
        return sum_head.next
            
        
                