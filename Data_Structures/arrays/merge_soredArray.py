"""  
Merge nums1 and nums2 into a single array sorted in non-decreasing order.

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
"""

def MergeMyTry(nums1, m, nums2, n):
    num_x = nums1[:m]
    num_y = nums2[:n]

    for j in range(len(num_y)):
        num_x.insert(len(num_x)+ j, num_y[j])
        j +=1

    num_x.sort()
    return num_x
    
# online solution...
def merge1(nums1, m, nums2, n):
    nums1[m:] = nums2[:n]
    return nums1


def merge2(nums1, m, nums2, n):
    while m> 0 and n>0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n -1] = nums1[m-1]
                m -=1
            else:
                nums1[m+n-1]= nums2[n-1]
                n -=1
        
    while n>0:
        nums1[m+n-1] = nums2[n-1]
        n -=1
    return nums1


# execution...
nums1 = [1,2,3,0,0,0]
m = 3 
nums2 = [2,5,6]
n = 3
answer = merge2(nums1, m, nums2, n)
print(answer)
