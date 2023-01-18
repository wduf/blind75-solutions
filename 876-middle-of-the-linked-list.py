# 93.29% time
# 95.59% memory

class Solution:
    def middleNode(self, fast: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
