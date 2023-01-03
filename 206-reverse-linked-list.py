# ITERATIVE
# 95.80% time
# 94.01% memory

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        prev = None
        while head.next:
            prev, head.next, head = head, prev, head.next
        head.next = prev
        return head
      
# RECURSIVE
# 98.05% time
# 8.24% memory

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def f(head: Optional[ListNode], prev: Optional[ListNode]) -> Optional[ListNode]:
            if not head:
                return prev
            next, head.next = head.next, prev
            return f(next, head)
        
        return f(head, None)
