"""
Given an integer array nums, return true if any value appears at least twice in the array,
 and return false if every element is distinct.

Input: nums = [1,2,3,1]
Output: true

"""

def containsDuplicate(nums):

    for i in range(len(nums)):
        for j in range(0, i):
            if nums[j] == nums[i]:
                return True
    return False


nums = [1,1,1,3,3,4,3,2,4,2]
nums1 = [1,2,4]
nums2 = []
print(containsDuplicate(nums2))