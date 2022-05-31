""""Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.
Example 1:
	Input:  nums = [1,0,1,1,0]
	Output:  4
	
	Explanation:
	Flip the first zero will get the the maximum number of consecutive 1s.
	After flipping, the maximum number of consecutive 1s is 4.

"""

def max_ones_2(nums):
    j = -1
    zero_count = 0
    answer = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            zero_count +=1
        
        while zero_count>1:
            j +=1
            if nums[j] ==0:
                zero_count -=1
        
        length = i-j
        if (length>answer):
            answer = length
    
    return answer

# execution...
nums = [1,0,1,0,1]

print(max_ones_2(nums))


