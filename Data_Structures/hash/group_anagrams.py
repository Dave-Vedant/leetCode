"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""

from collections import defaultdict

def groupAnagram(strs):
    ans = defaultdict()
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] +=1
        ans[tuple(count)].append(s)
    return ans.values()

    # time complexity = O(N*M), space complexity = O(N*M)

def groupAnagram1(strs):
    ans = defaultdict(list)
    print(ans)
    for s in strs:
        print(s)
        ans[tuple(sorted(s))].append(s)   # s= "eat" ==> tuple(s) ==> "e","a","t" ==> tuple(sorted(s)) ==> "a","e","t", .append(s) ==> word as value....
        print(ans)
        print("looooooooooooooop completed")
    return ans.values()


    # time complexity = O(N* klogk), space complexity = O(N*k)

# execution:
input = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagram1(input))


