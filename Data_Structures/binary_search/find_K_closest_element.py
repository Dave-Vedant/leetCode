# return the closest K element (k number of length) near to value x, from array arr.

def findClosestElement(arr, k, x):
    left = 0 
    right = len(arr)-k

    while left<right:
        mid = (left+right)//2
        if x-arr[mid]> arr[mid+k]-x:    # it gives the comparison of closest distance logic
            left = mid +1
        else:
            right = mid
    return arr[left:left+k]

    # time compolexity = O(log(N-K)+K), space complexity = O(1)



