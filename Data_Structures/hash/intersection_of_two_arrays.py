"""
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must be unique and you may return the result in any order.

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
"""

def set_interSection(set1, set2):
    for x in set1:
        if x in set2:
            return x

def interSection(nums1,nums2):
    set1 = set(nums1)
    set2 = set(nums2)

    if len(set1) < len(set2):            # for loop is on first set so, better to start with that set.
        return set_interSection(set1,set2)
    else:
        return set_interSection(set2, set1)

    # time compelity = O(N + M), space complexity = O(N+M)



## built-in set intersection

def interSection1(self, nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    return list(set2 & set2)

    # time complexity = O(n+m), space complexity = O(n+m)

    
