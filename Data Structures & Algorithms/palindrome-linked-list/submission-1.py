# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        first = head
        mid = slow
        second = None
        while mid:
            tmp = mid.next
            mid.next = second
            second = mid
            mid = tmp

        while first and second:
            if first.val != second.val:
                return False

            first = first.next
            second = second.next

        return True