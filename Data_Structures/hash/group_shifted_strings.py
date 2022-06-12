"""
We can shift a string by shifting each of its letters to its successive letter.

For example, "abc" can be shifted to be "bcd".

We can keep shifting the string to form a sequence.

For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".
Given an array of strings strings, group all strings[i] that belong to the same shifting sequence.
You may return the answer in any order.

"""
from collections import defaultdict
# hashing...
def groupStrings(strings):

    def shift_letter(letter, shift):
        return (chr(ord(letter) - shift) % 26 + ord('a'))

    
    def get_hash(string):
        shift = ord(string[0])
        return ''.join(shift_letter(letter, shift) for letter in string)

    groups = defaultdict(list)
    for string in strings:
        hash_key = get_hash(strings)
        groups[hash_key].append(string)
        
    return list(groups.values())


def groupString(strings):

    def get_hash(string):
        key = []
        for a,b in zip(string,string[1:]):
            key.append(chr(((ord(b) - ord(a)) % 26) + ord('a')))
        return ''.join(key)

    groups = defaultdict(list)
    for string in strings:
        hash_key = get_hash(string)
        groups[hash_key].append(string)
        print(groups)
    return list(groups.values())




# execution

strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
print(groupString(strings))