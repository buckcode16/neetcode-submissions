# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # runner gap
        fast = head
        slow = dummy = ListNode(0,head)
        for _ in range(n):
            fast = fast.next


        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next