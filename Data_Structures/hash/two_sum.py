"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have EXACTLY ONE SOLUTION, and you may not use the same element twice.

You can return the answer in any order.

"""
# brute Force
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[j] == target - nums[i]:
                return [i,j]
    
    # time complexity = O(N^2), space complexity = O(1)       
    
        i
# two-pass hashtable
def twoSum_2H(nums,target):
    hash_map = {}
    for i in range(len(nums)):      # generate hash_map and fill the value 
        hash_map[nums[i]] = i
    for i in range(len(nums)):      
        complement = target - nums[i]    # decide which element required, and try to find it. Also add another condition as "that element shold not be the same for which we are seraching. 10 = 5 + 5"
        if complement in hash_map and hash_map[complement] != i:          
            return [i, hash_map[complement]]
            
    # time complexity = O(N), space complexity = O(N)


# one-pass hashtable
def twoSum_1H(nums, target):
    hash_map = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hash_map:
            return [i, hash_map[complement]]
        hash_map[nums[i]] = i                       # if value is not in hashmap then we will add it, for later tracking. (we are adding the number as we go throgh the list, NOT the COMPLEMENT!)
    
    # time complexity = O(N), space complexity = O(N)
