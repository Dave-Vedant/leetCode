"""Given an integer array nums, return the third distinct maximum number in this array. 
If the third maximum does not exist, return the maximum number.

Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.

"""
def third_max(nums):
    unique_nums = list(set(sorted(nums)))
    print(unique_nums)
    if len(unique_nums) <3:
        return max(unique_nums)
    else:
        return unique_nums[-3]


# execution..
nums = [2,2,3,1]
print(third_max(nums))

