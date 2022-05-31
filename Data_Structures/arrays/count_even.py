"""Given an array nums of integers, return how many of them contain an even number of digits.

Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.
"""

def findNumbers(nums):
    count = 0
    for num in nums:
        if len(str(num))%2 == 0:
            count = count +1
    return count

def findNumber1(nums):
    event_elements = [num for num in nums if len(str(num))%2==0]
    return len(event_elements)

def findNumber2(nums):
    return [len(str(num))%2==0 for num in nums].count(True)

""" other logic"""
# my iniial logic...

def findNumberMine(nums):
    n = 0
    count = 0
    cur_count=0
    for n in range(5):
        for i in range(len(nums)):
            if (10^n <= nums[i] < 10^(n+1)) & (n%2!=0):
                cur_count +=1
            else:
                cur_count = cur_count
            i +=1
        count = count + cur_count
        n = n+1
    return count
                
# execution
nums = [12,345,2,6,7896]
answer = findNumber1(nums)
print(answer)