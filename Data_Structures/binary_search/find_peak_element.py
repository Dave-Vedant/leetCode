# find the any peak, and return the index of that

# iterative binary solution
def findPeakElement(nums):
    if not nums:
        return -1
    
    left= 0
    right = len(nums)-1

    while left<right:
        mid = left + (right-left)//2
        if nums[mid] > nums[mid-1] and nums[mid]>nums[mid+1]:
            return mid
        
        elif nums[mid] > nums[mid+1]:
            right = mid-1
        else:
            left = mid+1
    return left

    # time complexity : O(log(N)), space complexity = O(1)
