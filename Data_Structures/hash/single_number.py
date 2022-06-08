"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Input: nums = [2,2,1]
Output: 1
"""

# list approach...
def singleNumber(nums):
    no_duplicate_list = []
    for i in nums:
        if i in no_duplicate_list:
            no_duplicate_list.append(i)   #append the number for first time
        else:
            no_duplicate_list.remove(i)  # if same number came again, remove the number.
    return no_duplicate_list.pop()       # only, one number remain in list, which came for one time only and POP it.

# time complexity = O(N^2), space complexity = O(N)


# hash table...
from collections import defaultdict
def singleNumber(nums):
    hash_table = defaultdict(int)    # [ key: value = number: count]
    for i in nums:             
        hash_table[i] += 1       # repeat will add the count
    
    for i in hash_table:           # if count == 1 means single number
        if hash_table[i] == 1:
            return i

    # time complexity = O(n) , space complexity = O(n)

# math operation...
def singleNumber(nums):
    return 2 * sum(set(nums)) - sum(nums)

    # time compexity = O(N), space complexity = O(N)

# bit manipulation... (best solution...)
def singleNumber(nums):
    a = 0
    for i in nums:
        a ^= 1         # ^ is XOR operation... [1010 ^ 1010 ==> 0000 ]

    return a
    # time complexity = O(N), space complexity = O(1)



