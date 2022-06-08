def findTargetSumWays(nums, target):
    dp = {}

    def backtrack(i, total):
        # if we reach to end of array,
        if i == len(nums):
            return 1 if total == target else 0
        
        # if we see the index, pair total, then it must be in our cache
        if (i,total) in dp:
            return dp[(i,total)]

        # if any of above not done, then recuresive (either we add a value or subsract it (as per the allowed + or - operations))
        dp[(i,total)] = backtrack(i+1, total+nums[i]) + backtrack(i+1, total-nums[i])
        return dp[(i,total)]

    # calling backtracking function, start with (index,total) = (0,0) :(
    return backtrack(0,0)
