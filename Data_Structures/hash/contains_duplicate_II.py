"""
Given an integer array nums and an integer k, 
return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Input: nums = [1,2,3,1], k = 3
Output: true
"""


# Hashmap solution
def containsNearbyDuplicate(nums, K):
    hash_map = {} 
    for index, value in enumerate(nums):
        if (value in hash_map) and (index - hash_map[value] <= K):
            return True
        hash_map[value] = index
    return False

    # time complexity O(N), space complexity = O(min(N,K))
    

# execution:

nums = [1,2,3,1,2,3]
K =2
print(containsNearbyDuplicate(nums,K))