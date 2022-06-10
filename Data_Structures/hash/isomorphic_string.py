"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.

Input: s = "egg", t = "add"
Output: true

"""
## Approach 1: character mapping with dictionary:

from math import gamma
from numpy import take_along_axis


def isIsomorphic(s, t):
    mapST, mapTS = {}, {}
    
    for i in range(len(s)):
        print("enter to loop")
        c1, c2 = s[i], t[i]
        print(c1,c2)

        if ((c1 in mapST and mapST[c1] != c2) or  (c2 in mapTS and mapTS[c2] != c1)):

            """checking that c1 is not exist until yet, if it is exist...menas it came before as well during loop. 
                In such case that c1 also map some c2, right!?!. Ofcause, then check the c1-->c2 or not, if NO (!=) then answer is False."""                   
            return False
        
        mapST[c1] = c2
        mapTS[c2] = c1
        print(mapST, mapTS)
        print("===========looooooooop complete==================")
    return True

    # time complexity = O(N), space complexity = O(1)

## Approach 2: First Occurance Transformantion...
def transformString(s):
    index_mapping = {}
    new_str = []

    for i,c in enumerate(s):
        if c not in index_mapping:
            index_mapping[c] = i 
        new_str.append(str(index_mapping[c]))
    
    return " ".join(new_str)

def isIsomorphic1(s,t):
    return transformString(s) == transformString(t)

    # time complexity = O(N), space complexity = O(N)






# execution...

s = "boo"
t = "baa"  

print(isIsomorphic(s,t))