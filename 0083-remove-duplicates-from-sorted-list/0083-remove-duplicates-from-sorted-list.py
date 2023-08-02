# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        
        while dummy and dummy.next:
            while dummy.next and dummy.val == dummy.next.val:
                dummy.next = dummy.next.next
            
            dummy = dummy.next
        
        return head