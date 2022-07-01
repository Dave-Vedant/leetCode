# search in rotated sorted Array


# input : array (sorted but rotated after that)
# output : index on which it sorted

# binary Search Approach
def search_binary(nums, target):
    left, right = 0, len(nums)-1

    while left <= right:
        mid = (left+right)//2
        if target == nums[mid]:
            return mid

        if nums[left] <= nums[mid]:
            if target > nums[mid] or target < nums[left]:
                left = mid+1
            else:
                right = mid-1
        else:
            if target < nums[mid] or target > nums[right]:
                right = mid-1
            else:
                left = mid+1
    return -1
    # time complexity = O(log(N)), space complexity = O(1)

    
nums = [4,5,6,7,0,1,2]
target = 0

print(search_binary(nums, target))






