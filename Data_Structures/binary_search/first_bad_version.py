def firstBadVersion(n):
    left = 0
    right = n
    while (left<right):
        mid = left + (right-left)//2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid+1
    return left
    # time complexity = O(log(N)), space complexity = O(1)
# execution...
import random
def isBadVersion(n):
    return random.randint(0,n)

print(firstBadVersion(5))