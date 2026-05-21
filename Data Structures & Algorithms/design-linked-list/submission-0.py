class ListNode:
    def __init__(self, val, prev=None,next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head, self.tail = ListNode(0), ListNode(0)
        self.head.next, self.tail.prev = self.tail, self.head

        

    def get(self, index: int) -> int:

        cur = self.head.next

        i = 0
        while i < index and cur != self.tail:
            cur = cur.next
            i+=1

        return cur.val if cur != self.tail else -1



    def addAtHead(self, val: int) -> None:
        nxt, prv = self.head.next, self.head
        newNode = ListNode(val,prv,nxt)
        self.head.next = nxt.prev = newNode


    def addAtTail(self, val: int) -> None:
        nxt, prv = self.tail, self.tail.prev
        newNode = ListNode(val,prv,nxt)
        self.tail.prev = prv.next = newNode

    def addAtIndex(self, index: int, val: int) -> None:

        cur = self.head
        i = 0

        while i < index and cur != self.tail:
            cur = cur.next
            i+=1

        # revise 
        if cur == self.tail and i < index:
            return

        nxt = cur.next
        prv = cur
        newNode = ListNode(val, prv, nxt)
        
        prv.next = nxt.prev = newNode
        # revise end
            
    def deleteAtIndex(self, index: int) -> None:
        
        cur = self.head.next
        i = 0
        while i < index and cur != self.tail:
            cur = cur.next
            i += 1

        if cur == self.tail:
            return

        prv, nxt = cur.prev, cur.next
        prv.next = nxt
        nxt.prev = prv


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)