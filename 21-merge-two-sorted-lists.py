# 93.19% time
# 79.20% memory

class Solution:
    def mergeTwoLists(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        # o(n) time
        # o(1) space
        pre = itr = ListNode()
        while head1 and head2:
            if head1.val > head2.val:
                itr.next = head2
                itr, head2 = itr.next, head2.next
            else:
                itr.next = head1
                itr, head1 = itr.next, head1.next
        if head1:
            itr.next = head1
        elif head2:
            itr.next = head2
        return pre.next
