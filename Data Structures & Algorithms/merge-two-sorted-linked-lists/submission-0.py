# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        c1,c2 = list1,list2
        d = ListNode()
        t = d

        while c1 and c2:
            if c1.val < c2.val:
                t.next = c1
                t = t.next
                c1 = c1.next
            else:
                t.next = c2
                t = t.next
                c2 = c2.next

        if c1:
            t.next = c1
        else:
            t.next = c2


        return d.next