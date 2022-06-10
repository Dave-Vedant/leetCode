"""
  Intersection of Two Arrays II

Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

"""

def intersect(nums1, nums2):
    i = 0
    j = 0
    result = []
    sorted(nums1), sorted(nums2)

    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            result.append(nums1[i])
            i +=1
            j +=1
        elif nums1[i] < nums2[j]:
            i +=1
        else:
            j +=1
    return result

    # time complexity = O(NlogN)), space complexity = O(N) 

from collections import Counter
def interSect1(nums1, nums2):
    a,b = map(Counter, (nums1, nums2))
    return list((a&b).elements())


def intersect2(nums1, nums2):
    count1 = Counter(nums1)
    count2 = Counter(nums2)

    keyList = [i for i in count1.key() if i in count2.key()]
    for i in count1.key():
        if i in count2.key():
            keyList = [i]

    for key in keyList:
        interList += [key] * min(count1.get(key), count2.get(key))
    return interList


def intersect(nums1, nums2):
    c = Counter(nums1)
    result = []
    for n in nums2:
        if c[n] >0:
            result.append(n)
            c[n] -=1
        return result
    # time complexity = O(N+M), space complexity = O(N)



    



# execution...
nums1 = [1,2,2,1]
nums2 = [2,2]

print(interSect1(nums1, nums2))
