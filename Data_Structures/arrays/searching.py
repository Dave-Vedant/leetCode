"""Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

Input: arr = [10,2,5,3]
Output: true
Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.

"""

def check_double(arr):
    existance = False
    for i in range(len(arr)):
        for j in range(len(arr)):
            if (arr[i] == 2 * arr[j]) & (i!=j):
                existance = True
                exit
            
    return existance



# execution...
arr = [7,1,14,11]
test1 = check_double(arr)
#print(test1)

arr2 = [-2,0,10,-19,4,6,-8]
test2 = check_double(arr2)
# print(test2)

arr3 = [0,0]
test3 = check_double(arr3)
print(test3)
