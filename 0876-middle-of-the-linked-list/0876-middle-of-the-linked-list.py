class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c = 0
        tmp = head
        while tmp:
            c+=1
            tmp = tmp.next
            
        c = c//2
        l = 0
        while l < c:
            head = head.next
            l+=1
        return head
        