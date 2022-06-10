





# Naive Linear Approach:

def containsNearbyDuplicate(nums, k):
    for i in range(len(nums)):
        for j in range(0, i):
            if nums[i] == nums[j]:
                return True
    return False

    #time complexity = O(N*min(K,N)), space complexity = O(1)

# Hashmap solution
def contansNearbyDuplicate(nums, K):
    hash_map = {} 
    for i,v in enumerate(nums):
        if (v in hash_map) and (i - hash_map[v] <= K):
            return True
        hash_map[v] = i
    return False

    # time complexity O(N), space complexity = O(min(N,K))
    

# jexecution:

nums = [1,2,3,1,2,3]
K =2
print(containsNearbyDuplicate(nums,K))