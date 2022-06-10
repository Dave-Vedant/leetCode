"""
Given a string s, find the first non-repeating character in it and return its index. 
If it does not exist, return -1.

Input: s = "leetcode"
Output: 0

"""
from collections import Counter

def firstUniqueChar(s):
    count = Counter(s)

    for i, ch in enumerate(s):
        if count[ch] ==1:
            return i
    return -1

    # time complexity = O(N), space complexity = O(1)

s = "leetcodel"
print(firstUniqueChar(s))

                