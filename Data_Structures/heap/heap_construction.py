# construct Heap (min heap)
# space for whole solution is ... O(1) for time complexity depends on operation...
class MinHeap:

    def __init__(self, array):
        self.heap = self.buildHeap(array)
    
    # O(N)
    def buildHeap(self,array):
        firstParentIndex = (len(array) -1)//2
        for currentIndex in reversed(range(firstParentIndex)):
            self.shiftDown(currentIndex, len(array)-1, array)
        return array

    # O(log(N)) 
    def shiftDown(self, currentIndex, endIndex, heap):
        childOneIndex = currentIndex *2 +1
        while  childOneIndex <=  endIndex:
            childTwoIdex = currentIndex * 2 + 2 if currentIndex  * 2 + 2 <=endIndex else -1
            if childTwoIdex != -1 and heap[childTwoIdex] < heap[childOneIndex]:
                idxToSwap = childTwoIdex
            else:
                idxToSwap = childOneIndex
            if heap[idxToSwap] < heap[currentIndex]:
                self.swap(currentIndex, idxToSwap, heap)
                currentIndex = idxToSwap
                childOneIndex = currentIndex * 2 + 1
            else:
                break
    # O(log(N))
    def shiftUp(self, currentIndex, heap):
        parentIndex = (currentIndex-1)//2
        while currentIndex > 0 and heap[currentIndex] < heap[parentIndex]:
            self.swap(currentIndex, parentIndex, heap)
            currentIndex = parentIndex
            parentIndex = (currentIndex-1)//2
    # O(1)
    def peek(self):
        return self.heap[0]

    # O(log(N))
    def remove(self):
        self.swap(0,len(self.heap) -1, self.heap)
        valueToRemove = self.heap.pop()
        self.shiftDown(0,len(self.heap)-1, self.heap)
        return valueToRemove

    # O(log(N))
    def insert(self, value):
        self.heap.append(value)
        self.shiftUp(len(self.heap)-1, self.heap)
        
    # O(log(N))
    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]