"""
Given an integer array nums, return true if any value appears at least twice in the array,
 and return false if every element is distinct.

Input: nums = [1,2,3,1]
Output: true

"""
# Naive Linear Search O(N^2)
def containsDuplicate_NLS(nums):

    for num in nums:
        for j in range(0,num):
            if nums[j] == nums[num]:
                return True
    return False
    # time complexity = O(N^2), space complexity = O(1).

# sorting 
def containDuplicate_sorting(nums):
    sorted(nums)
    for num in nums:
        if nums[num] == nums[num+1]:
            return True
    return False
    # time complexity = O(NlogN), space complexity = O(1)


# hash table
def containDuplicate_hashTable(nums):
    hash_set = set()
    for num in nums:
        if num in hash_set:
            return True
            break
        hash_set.add(num)
    return False
 
    # time comlexity =O(N), space complexity =O(N)

# execution...
nums = [1,1,1,3,3,4,3,2,4,2]
nums1 = [1,2,4]
nums2 = []
print(containsDuplicate_NLS(nums2))