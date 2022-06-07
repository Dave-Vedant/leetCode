"""
Main concerns:

- solution need to be : O(1)
- Min stack does not mean to pop the last element
- solution is wi=thout the consideration of invalid case.

"""
# Approach: Stock of value

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self,x):
        if not self.stack:
            self.stack.append((x,x))
            return
        curr_min = self.stack[-1][1]
        self.stack.append((x,min(x,curr_min)))          # setting up like this, will give us ease to get min / max element
    
    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return self.stack[-1][1]

    def getMax(self):            # this is not O(1) time complex...
        max_side = self.stack[0]
        return max(max_side)
    # time complexity = O(1), space complexity = O(n)


# Approach: Two stack

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self,x):
        self.stack.append(x)
        if not self.min_stack or x<= self.min_stack[-1]:
            self.min_stack.append(x)
        
    def pop(self):
        if self.stack[-1] == self.stack[-1]:
            self.min_stack.pop()
        self.stack.pop()
    
    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]

    # time complexity = O(1), sapce complexity = O(n)


# Improved Two Stacks:
"""
beside of tracking min val only, will track the tuple of last to [new_min_val, count_of_min_value]...
"""
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self,x):
        self.stack.append(x)

        if not self.min_stack or x< self.stack[-1][0]:
            self.min_stack.append([x,1])
        elif x == self.min_stack[-1][0]:
            self.min_stack[-1][1] +=1          # this condition, will increase the "1" position which represnet howmany time the min value counted.
        
    def pop(self):
        if self.min_stack[-1][0] == self.stack[-1]:
            self.min_stck[-1][1] -= 1              # decrease the count, and  then next if loop

        if self.min_stack[-1][-1] == 0:      # if the count goes zero then remove that min tracker value
            self.min_stack.pop()
        
        self.stack.pop()
    
    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        return self.min_stack[-1][0]

    # time complexity = O(1), space complexity = O(n) 



    