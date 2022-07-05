class TrieNode:

    def __init__(self):
        self.children = {} # hashmap // dictionary
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        cur = self.root
        for ch in len(word):
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.word = True

    def search(self, word):

        def dfs(j,root):
            cur = root
            for i in range(j,len(word)):
                ch = word[i]

                if ch == ".":
                    for child in cur.children.values:
                        if dfs(i+1, child):
                            return True
                    return False

                else:
                    if ch not in cur.children:
                        return False
                    cur =  cur.children[ch]
            return cur.word
        
        dfs(0, self.root)

        # time complexity = O(M) - keylength [M:N] 
        # # space complexity = O(M), [ in worst case, each word we add not present already, 
        # So, we need to add as new key, so ultimatly New keys (M) is complexity]



"""
# Alternate Solution: 

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        def dfs(i, node):
            if i==len(word):
                return node.endOfWord
            if word[i] == ".":
                for child in node.children.values():
                    if dfs(i+1, child):
                        return True
            if word[i] not in node.children:
                return False
            else:
                return dfs(i+1, node.children[word[i]])
            
        ans = dfs(0, cur)
        return ans


"""


            



        
