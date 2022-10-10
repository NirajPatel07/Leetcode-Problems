# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        stack = []
        temp = head
        
        while temp:
            stack.append(temp)
            temp = temp.next
        
        head = temp = stack.pop()
        while len(stack)>0:
            temp.next = stack.pop()
            temp = temp.next
        
        temp.next = None
        return head