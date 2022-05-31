class node:

    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None

    def getLength(self):
        count = 0
        iterator = self.head
        while iterator:
            count +=1
            iterator = iterator.next
        return count

    def get(self, index):
        length = self.getLength()
        if index+1>length or index < 0:
            return -1
        elif index ==0:
            return self.head.val
        else:
            count = 0
            iterator = self.head
            while iterator.next:
                count +=1
                if count == index:
                    return iterator.next.val
                iterator = iterator.next
    
    def addAtHead(self,val):
        new_node = node(val)
        new_node.next = self.haed
        self.head = new_node

    def addAtTail(self,val):
        new_node = node(val)

        if self.head == None:
            self.head = new_node
        iterator = self.head
        while iterator.next:
            iterator = iterator.next
        iterator.next = new_node
    
    def addAtIndex(self, index, val):
        length = self.getLength()
        
        if index> length:
            return 'index is invalid'
        
        if index ==0:
            new_node = node(val)
            new_node.next = self.head
            self.head = new_node
        else:
            count = 0
            iterator = self.head
            while iterator:
                count +=1
                if count == index:          # this will done when we reach upto given index
                    new_node = node(val)
                    new_node.next = iterator.next
                    iterator.next = new_node
                iterator = iterator.next

    def deleteAtIndex(self, index):
        iterator = self.head
        length = self.getLength()
        if index>length:
            return 'invalid index'
        elif index ==0:
            self.head = iterator.next
        else:
            count = 0

            while iterator.next:
                count +=1
                if count == index:
                    iterator.next = iterator.next.next
                    break

                iterator = iterator.next
                 
