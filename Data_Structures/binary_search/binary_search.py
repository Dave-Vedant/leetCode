"""
Given an array of integers nums which is sorted in ascending order, 
and an integer target, write a function to search target in nums. 

If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.


Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
"""

def search(nums, target):
    # initialize left and right
    left, right = 0, len(nums)-1
    while left <= right:
        # find the midean (pivot)
        pivot = left + (right - left) //2
        # find that the pivot'value is == target?
        if target == nums[pivot]:
            return pivot
        # Is the target value lower than pivot? --> 
        # if so increament or decrement the value of right and left based on pivot
        if target < nums[pivot]:
            right = pivot - 1
        else:
            right = pivot + 1
    # exception then return -1
    return -1


    # time complexity = O(log(N)), space complexity = O(1)


