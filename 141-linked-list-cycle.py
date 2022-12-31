# 98.93% time
# 67.01% memory

class Solution:
    def hasCycle(self, fast: Optional[ListNode]) -> bool:
        # changed arg name head -> fast
        slow = fast
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow is fast:
                return True
        return False
