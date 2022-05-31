def duplicateZerosMyTry(nums):
    return_nums = []
    max_length = len(nums)
    for i in range(len(nums)):
        if nums[i] == 0:
            return_nums.append(0)
        else:
            return_nums.append(nums[i]) 
        if len(return_nums) > max_length:
            exit
        i +=1       
    return return_nums



def duplicateZeros(nums):
    i = 0
    while i < len(nums) -1:
        if nums[i] ==0:
            nums.insert(i+1, 0)
            del nums[len(nums)-1]
            i = i + 2
        else:
            i = i +1
    return nums


# execution...
arr = [1,0,2,3,0,4,5,0]
result = duplicateZeros(arr)
print(result)