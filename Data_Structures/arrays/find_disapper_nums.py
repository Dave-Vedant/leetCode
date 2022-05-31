"""Given an array nums of n integers where nums[i] is in the range [1, n], 
return an array of all the integers in the range [1, n] that do not appear in nums.

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
"""

def findDisappearNums(nums):
    pointer = 1
    sorted_nums = sorted(list(set(nums)))
    # print(sorted_nums)
    missing_nums = []

    for i in range(len(sorted_nums)):
        if sorted_nums[i] != pointer:
            # print("appending value : ", pointer)
            missing_nums.append(pointer)
        pointer +=1
        #else:
            #print("escaping...... ", sorted_nums[i])
        
    if missing_nums == []:
        missing_nums.append(sorted_nums[-1]+1)

    return missing_nums
                
                

# execution..
nums = [4,3,2,7,8,2,3,1]
#nums = [1,1]
print(findDisappearNums(nums))