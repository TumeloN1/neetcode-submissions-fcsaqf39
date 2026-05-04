# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) 
        fast, slow = dummy, dummy

        # advance fast by n+1 steps
        for _ in range(n + 1):
            fast = fast.next

        # move both until fast is None
        while fast:
            fast = fast.next
            slow = slow.next

        # slow is now just BEFORE the node to delete
        slow.next = slow.next.next

        return dummy.next