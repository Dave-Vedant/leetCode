from math import e, log

def mysqrt(x):
    if x<2:
        return x
    
    left = int(e**(0.5 * log(x)))  
    right = left +1
    return left if right * right > x else right
# time complexity = O(1), space complexity = O(1)

#binary search...
def mySqrt(x):
    if x<2:
        return x
    
    left, right = 2, x//2

    while left <= right:
        pivot = left + (right - left)//2
        num = pivot * pivot
        if num >x:
            right = pivot -1
        elif num <x:
            left = pivot + 1
        else:
            return pivot
    return right
    # time coplexity = O(log(N)), space complexity = O(1)