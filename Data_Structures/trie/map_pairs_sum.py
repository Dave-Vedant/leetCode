# hash_map
import collections
class MapSum:
    def __init__(self):
        self.map = {}
        self.score = collections.Counter()
    
    def insert(self, key, val):
        delta = val - self.map.get(key,0)
        self.map[key] = val
        for i in range(len(key)+1):
            prefix = key[:i]
            self.score[prefix] += delta
        
    def sum(self,prefix):
        return self.score[prefix]
        # tiem complexity = O(N^2), space com;exity = O(N)


# Trie...

class TrieNode:
    def __init__(self):
        self.children = {}
        self.score = 0

class MapSum:

    def __init__(self):
        self.children = {}
        self.score = 0

    def insert(self, key, val):
        delta = val - self.map.get(key,0)
        self.map[key] = val
        cur = self.root
        cur.score += delta
        for char in key:
            cur = cur.children.setdefault(char, TrieNode())
            cur.score = delta

    def sum(self, prefix):
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return 0
            cur = cur.children[char]
        return cur.score


    # time complexity = O(N), space complexity = O(N)