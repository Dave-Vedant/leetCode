"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1  ===> sum of end up digit square is == 1

Input: n = 2
Output: false

"""
## Approach 1: division and modulo + HashSet

def isHappy_stack(n):

    def get_next(n):
        total_sum = 0
        while n>0:
            n, digit = divmod(n,10)
            total_sum += digit **2
        return total_sum

    visited = set()
    while n!= 1 and n not in visited:         # seecond codition to remove the posibility of circular stuck.
        visited.add(n)
        n = get_next(n)

    return n == 1
    # time complexity = O(logN), space complexity = O(logN)


## Approach 2: divmod + Floyd algorithm
def isHappy_floyd(n):

    def get_next(n):
        total_sum = 0
        while n > 0:
            n, digit = divmod(n,10)
            total_sum += digit**2
        print(total_sum)
        return total_sum

    slow_runner = n
    fast_runner = get_next(n)
    while fast_runner != 1 and slow_runner != fast_runner:
        slow_runner = get_next(slow_runner)
        fast_runner = get_next(get_next(fast_runner))
    return fast_runner ==1

    # time complexity = O(logN), sapce complexity = O(1)


## Approach 3: divmod + math solution....
def isHappy_math(n):
    cycle_member = {4, 16, 37, 58, 89, 145, 42, 20}

    def get_next(n):
        total_sum = 0
        while n > 0:
            n, digit = divmod(n, 10)
            total_sum += digit**2
        return total_sum
    
    while n != 1 and n not in cycle_member:
        n = get_next(n)
    
    return n == 1

    # time complexity = O(logN), space complexity = O(1)


# execution...
n= 19
print(isHappy_floyd(n))