from re import X


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None

class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index):
        if index<0 or index>self.size:
            return -1

        if index+1 < self.size - index:
            curr = self.head
            for _ in range(index+1):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - index):
                curr = curr.prev
        return curr.val
    
    def addAtHead(self, val):
        pred, succ = self.head, self.head.next
        self.size += 1
        new_node = ListNode(val)
        new_node.prev = pred
        new_node.next = succ
        pred.next = new_node
        succ.prev = new_node

    def addAtTail(self, val):
        pred, succ = self.tail.prev, self.tail
        self.size +=1
        new_node = ListNode(val)
        new_node.prev = pred
        new_node.next = succ
        pred.next = new_node
        succ.prev = new_node

    def addAtIndex(self, index, val):
        if index > self.size:
            return
        
        if index<0:
            index = 0

        if index<self.size - index:
            pred = self.head
            for _ in range(self.size - index):
                succ = succ.prev
            pred = succ.prev

        self.size +=1

        new_node = ListNode(val)
        new_node.prev = pred
        new_node.next = succ
        pred.next = new_node
        succ.next = new_node

    def deleteAtIndex(self, index):
        if index<0 or index>= self.size:
            return
        
        if index<self.size - index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next.next
        else:
            succ = self.tail
            for _ in range(self.size - index- 1):
                succ = succ.prev
            pred = succ.prev.prev
        
        self.size -=1
        pred.next = succ
        succ.prev = pred
          