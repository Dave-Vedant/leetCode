def searchRange(nums, target):
    left=binSearch(nums,target,True)
    right=binSearch(nums,target,False)
    return [left,right]


def binSearch(nums, target, leftBias):
    left = 0
    right = len(nums)-1
    i=-1


    while left<=right:
        mid = (left+right)//2
        if target > nums[mid]:
            left = mid+1               # move to right
        elif target<nums[mid]:
            right = mid-1              # move to left
        else:
            i = mid
            if leftBias:
                right = mid-1     # move to left
            else:
                left = mid+1       # move to right
    return i

# execution..
nums = [5,7,7,8,8,10]
target = 8
print(searchRange(nums,target))

nums1 = [5,7,7,8,8,10]
target1 = 6
print(searchRange(nums1,target1))