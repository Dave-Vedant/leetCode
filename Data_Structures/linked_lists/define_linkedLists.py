from platform import node
from re import A


class Node(object):

    def __init__(self,val):
        self.val = val
        self.next = None

# linked list
class MyLinkedList:
    
    def __init__(self, index):
        self.head = None
        self.size = 0

    def get(self, index):
        if index <0 or index>= self.size:
            return -1
        
        if self.head is None:
            return None

        curr = self.head
        for i in range(index):
            curr = curr.next        # will next up to index value and return it.
        return curr.val


    def addAtHead(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node


    def addAtTail(self, val):
        curr = self.head             # this represent first element
        if curr is None:
            self.head = Node(val)    # if [] list then, new value is new head
        else:
            while curr.next is not None:    #until we can not reach the last element.. 
                curr = curr.next         # run the next
        curr.next = Node(val)           # when it will done, defin the next as new element and link it.


    def addAtIndex(self, index, val):
        if index<0 or index>self.size:
            return -1
        
        if index ==0:
            self.addAtHead(val)
        else:
            curr = self.head
            for i in range(index-1):
                curr=curr.next
            node = Node(val)
            node.next = curr.next
            curr.next = node

            self.size += 1
    

    def deleteAtIndex(self, index):
        if index<0 or index>=self.size:
            return -1
        
        curr = self.head
        if index ==0:
            self.head = curr.next
        else:
            for i in range(index-1):
                curr = curr.next
            curr.next = curr.next.next
        
        self.size -= 1



def test(x):
    if x != 1:
        return -1
    return 1
    
x = 2
print(test(x))


    


