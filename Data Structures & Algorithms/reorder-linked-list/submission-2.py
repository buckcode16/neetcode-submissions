# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        fast,slow = head.next, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next


        node = slow.next
        prev = slow.next = None

        while node:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp

        first = head
        second = prev

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
