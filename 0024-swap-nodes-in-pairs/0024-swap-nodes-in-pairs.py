class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        prev, cur = dummy, head
        while cur and cur.next:
            prev.next, cur.next = cur.next, cur.next.next
            prev.next.next = cur
            prev, cur = cur, cur.next
        return dummy.next