# 12 = 4 + 4 + 4 (output = 3 (number of perfect squeres))
# 13 = 4 + 9 (ouput = 2)

"""
Approach: 

Greedy Algo: Its not a greedy problem, because if we go greedy then alternative solution for 12 is : 9 + 1 +1 +1 = ouptut = 4)

brute force Approach: from 0 we can generate the branches, and go trough all the possible solution, and decide the smallest steps to target. But, its about the complexity


So, I will use the dynamic programming solution...
Logic:

divide main problem to sub solution using bottomup dyanmic approach. Explain in images folder with (perfect-squre.png)
"""

# Dynamic programming approach...
def numSqures(n):

    dp = [n] * (n+1)
    dp[0] = 0

    for target in range(1,n +1):
        print("target = ", target)
        for s in range(1, target+1):
            print("s = ", s)
            squre = s * s
            if target - squre <0:
                print("-=-=-=- break -=-=-=-")
                break
            dp[target] = min(dp[target], 1 + dp[target-squre])
            print("dp = ", dp)
            print("dp[target]", dp[target])
            print("complete One S loop")
        print("complete one target loop")
        print("=================")
    return dp[n]

    # time complexity = O(n*n^1/2), space complexity = O(n)


# brute force approach...











# execution...
print(numSqures(12))

