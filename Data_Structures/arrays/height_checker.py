"""A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in non-decreasing order by height. Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.

You are given an integer array heights representing the current order that the students are standing in. Each heights[i] is the height of the ith student in line (0-indexed).

Return the number of indices where heights[i] != expected[i].

Input: heights = [1,1,4,2,1,3]
Output: 3
Explanation: 
heights:  [1,1,4,2,1,3]
expected: [1,1,1,2,3,4]
Indices 2, 4, and 5 do not match. ==> so 3 is the answer...

"""
def height_check(h):
    count = 0
    for i in range(len(h)):
        if h[i] != sorted(h)[i]:
            count +=1
    return count

def height_check1(h):
    count = 0
    for a,b in zip(h, sorted(h)):
        if a != b:
            count +=1
    return count

def height_check2(h):
    return sum(a!=b for a,b in zip(h,sorted(h)))

# execution...
heights = [5,1,2,3,4]
print(height_check2(heights))