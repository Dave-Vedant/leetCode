"""
Input
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 3, true, true, true, 4]

Explanation
MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False
myCircularQueue.Rear();     // return 3
myCircularQueue.isFull();   // return True
myCircularQueue.deQueue();  // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear();     // return 4

Constraints:

1 <= k <= 1000
0 <= value <= 1000
At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty, and isFull
"""
# Array Approach:

class MyCircularQueue:
    def __init__(self, k):
        self.queue = [0] *k
        self.headIndex = 0
        self.count = 0
        self.capacity = k

    def enQueue(self, value):
        if self.count == self.capacity:
            return False
        
        self.queue[(self.headIndex + self.count) % self.capacity] = value
        self.count +=1 
        return True

    def deQueue(self):
        if self.count == 0:
            return False
        
        self.headIndex = (self.headIndex +1) % self.capacity
        self.count -=1
        return True
    
    def Front(self):
        if self.count == 0:
            return -1
        return self.queue[self.headIndex ]

    def Rear(self):
        if self.count == 0:
            return -1
        return self.queue[(self.headIndex + self.count -1) % self.capacity]

    def isEmpty(self):
        return self.count == 0
    
    def isFull(self):
        return self.count == self.capacity


# singly Linked List:
class Node:
    def __init__(self, value, nextNode = None):
        self.value = value
        self.next = nextNode

class MyCircularQueue:
    def __init__(self, k):
        # head, tail, count=length, capacity = k 
        self.capacity = k
        self.head = None
        self.tail = None
        self.count = 0

    def enQueue(self, value):
        if self.count == self.capacity:
            return False
        
        # check the count, if count is zero --> no node then introduce node and define as head
        if self.count == 0:
            self.head = Node(value)
            self.tail = self.head
        else:
            # if list exist, then define node and give define as tail, make "next" relationship
            newNode = Node(value)
            self.tail.next = newNode
            self.tail = newNode
        self.count +=1
        return True

    def deQueue(self):   
        # move head to next  
        if self.count == 0:
            return False
        self.head = self.head.next
        self.count -=1
        return True
    
    def Rear(self):
        # return the value of tail
        if self.count ==0:
            return -1
        return self.tail.value
    
    def Front(self):
        # return the value of head
        if self.count ==0:
            return -1
        return self.head.value
    
    def isEmpty(self):
        # count 0
        return self.count == 0

    def isFull(self):
        # count to full capacity
        return self.count == self.capacity
    
    # time complexity = O(1), space complexity = O(n)




        