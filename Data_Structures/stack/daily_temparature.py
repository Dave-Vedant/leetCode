"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

"""
# brute force solution...
from re import T


def dailyTemperatrues(tempratures):

    answer = [0] * len(tempratures)

    for day in range(len(tempratures)):
        for future_day in range(day+1, len(tempratures)):
            if tempratures[future_day] > tempratures[day]:
                answer[day] = future_day - day
                break
    
    return answer
    # time comlexity = O(n^2), space complexity = O()


# Mononic stack (monotonic means decreasing or eqaly order) ... reduce time complexity...

def dailyTemperatures1(temparature):

    result = [0] * len(temparature)
    stack = []    # [temperature, index]

    for i,t in enumerate(temparature):
        while stack and t > stack[-1][0]:             # last row, 2nd column (1)
            #print("stack elelment : ", stack[-1][0])
            stackT, stackInd = stack.pop()
            result[stackInd] = i - stackInd
        stack.append([t,i])
        #print(stack)
    return result

    # time complexity = O(n), space complexity = O(n) --->? O(1) is constant time where the O(n) is linear time complexity.


# Array, optimized sapce solution...
def dailyTemperatrues2(temperatures):
    n = len(temperatures)
    hottest = 0
    answer = [0] * n

    for i in range(n-1, -1, -1):
        t = temperatures[i]
        if t >= hottest:
            hottest = t 
            continue

        days = 1
        while temperatures[i + days] <= t:
            days += answer[i + days]
        answer[i] = days
    
    return answer

    # time complexity = O(n), space complexity = O(1)








input = [73,74,75,71,69,72,76,73]   
print(dailyTemperatures1(input))