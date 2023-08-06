# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hashmap={}
        
        while headA:
            hashmap[headA]=1
            headA=headA.next
            
        while headB and headB not in hashmap:
            headB=headB.next
            
        return headB