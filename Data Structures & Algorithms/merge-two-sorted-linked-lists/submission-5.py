# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Operation is structure
        # Engine is zipper
        # Volatile head yes

        dummy = ListNode(0)
        zipper = dummy

        while list1 and list2:
            if list1.val < list2.val:
                zipper.next = list1
                list1 = list1.next
            else:
                zipper.next = list2
                list2 = list2.next

            zipper = zipper.next

        zipper.next = list1 or list2

        return dummy.next