"""
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Input: arr = [2,1]
Output: false

Input: arr = [0,3,2,1]
Output: true
"""

# my solution...
def valid_mountain(arr):
    valid = False
    if len(arr) < 3:
        print("check the lenght is more than 3")
        exit()
        
    top = arr.index(max(arr))
    print("top : ", top)
    if arr[top] == arr[len(arr)-1]:
        print("check the last element is not max")
        exit()
    
    half_left = False
    half_right = False
    for i in range(len(arr[0:top])):  
        if arr[i] <= arr[i+1]:
            half_left = True
        else:
            exit()
    print('half_left', half_left)


    arr1 = arr[top:(len(arr))]
    print("arr1 : ", arr1)
    for j in range(len(arr1)-1):     
        if arr1[j] >= arr1[j+1]:
            half_right = True
        else:
            return 0
            exit()
    print('half_right', half_right)    

    if (half_left== half_right ==True):
        valid = True
    
    return valid

# solution...
# approach: GO FOR FLASE CONDITIONS, IF NOT IT WILL BE TRUE
def valid_mountain1(arr):
    top = 0
    # check minimum asking length
    if len(arr)<3:
        return False

    # get the first pick of array
    for i in range(len(arr)-1):
        if arr[i] >= arr[i+1]:
            top = i
            break
    
    # check the top is not the last element or not zero
    if (top == len(arr)-1) or top ==0:
        return False

    # check the values after our first pick is constently decreasing
    j = top
    for j in range((len(arr)-1)-top):
        if arr[top+j] <= arr[top+j+1]:
            return False
    
    return True
   # this does not work for one example, but the logic work in java (can not find python issue) ..

# real solution...
def valid_Mountain_Array(arr):
    n = len(arr)

    if n<3:
        return False
    
    increase = False
    decrease = False
    prev = arr[0]

    for i in arr[1:]:
        if i==prev:
            return False
        
        if i>prev:             # if next element is greater
            if decrease:
                return False
            increase = True          # change the inc value
        else:
            if not increase:
                return False
            decrease = True
        prev = i                   # update previous
    return  increase and decrease          # and operation (true and true == true (final))


# execution...
arr1 = [2,1]

arr2 = [3,5,5]

arr3 = [0,3,2,1]

arr4 = [1,3,2]

arr5 = [0]

arr6 = [1,7,9,5,4,1,2]

arr7 = [1,1,1,1,1,1,1,2,1]


#test = [arr1, arr2, arr3, arr4, arr5, arr6, arr7]
test = [arr2]
for i in range(len(test)):
    print("test ", i, ": ", valid_Mountain_Array(test[i]))
