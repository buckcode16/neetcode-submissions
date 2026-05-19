# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next



        prev = None
        mid = slow.next
        slow.next = None

        while mid:
            tmp = mid.next
            mid.next = prev
            prev = mid
            mid = tmp

        rev = prev

        # merge
        first, second = head, rev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

        


