"""Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

"""

def sortedSquaresMe(nums):
    square_list = []
    for num in nums:
        square = num*num
        square_list.append(square)
        num +=1
    square_list.sort()
    return square_list


def sortedSqure(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] * nums[i]
    nums.sort()
    return nums


# execution

nums = [0,1,9,16,100]
result = sortedSquaresMe(nums)



def sortedSquares(nums):
        # Non-optimal algorithm
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]
        nums.sort()
        return nums