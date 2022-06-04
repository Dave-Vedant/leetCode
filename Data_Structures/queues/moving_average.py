"""
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Implement the MovingAverage class:

MovingAverage(int size) Initializes the object with the size of the window size.
double next(int val) Returns the moving average of the last size values of the stream.


Example 1:

Input
["MovingAverage", "next", "next", "next", "next"]
[[3], [1], [10], [3], [5]]
Output
[null, 1.0, 5.5, 4.66667, 6.0]

Explanation
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1); // return 1.0 = 1 / 1
movingAverage.next(10); // return 5.5 = (1 + 10) / 2
movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3

"""
# Array or List...
def MovingAverage(size):
    queue = []
    queue.append(size)
    window_sum = sum(queue[-size:])
    return window_sum/min(len(queue),size)
    
    # time complexity = O(N), space complexity = O(M)

# double ended queue
from collections import deque

class MovingAverage:
    def __init__(self, size):
        self.size = size
        self.queue = deque()
        self.window_sum = 0
        self.count = 0

    def next(self, val):
        self.count +=1
        self.queue.append(val)
        if self.count > self.size:
            tail = self.queue.popleft()
        else:
            tail = 0
        self.window_sum = self.window_sum - tail + val
        return self.window_sum/ min(self.size, self.count)

    # time complexity = O(1), space complexity = O(n)

# circular queue with array:

class MovingAvereage:

    def ___init__(self, size):
        self.size = size
        self.front = 0
        self.window_sum = 0
        self.count = 0
        self.queue = [0] * self.size
    
    def next(self,val):
        self.count +=1
        rear = (self.front +1) % self.size
        self.window_sum = self.window_sum - self.queue[rear] + val
        self.front = (self.front +1) % self.size
        self.queue[self.front] = val
        return self.window_sum/ min(self.size, self.count)


    
    # time complexity = O(1), space complexity = O(n)





