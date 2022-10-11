# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
            fast ,slow = head ,head
    
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

                if slow == fast:  #cycle

                    slow = head
                    while fast != slow:
                        slow = slow.next
                        fast = fast.next         
                    return fast #return "fast or slow" : same node

            return None  #not a cycle