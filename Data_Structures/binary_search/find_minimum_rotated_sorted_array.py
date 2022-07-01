# return index of minimum of rotated array

"""
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

"""

def findMin(nums):
    result = nums[0]
    left =0
    right = len(nums)-1

    while left<=right:
        if nums[left] < nums[right]:
            result = min(result, nums[left])
            break
            
        mid = (left+right)//2
        result = min(result, nums[mid])
        if nums[mid] >= nums[left]:
            left = mid+1
        else:
            right = mid -1

    return result
        
