# trie is also called prefix tree

class TrieNode:

    def __init__(self):
        self.word = None
        self.children = {}    # hash map // dictionary // key:value


class Trie:

    def __init__(self):
        self.root = TrieNode()
        
        
    # insert
    def insert(self,word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c]= TrieNode()
            node = node.children[c]
        node.word = True
    

    # search
    def search(self,word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.word
    
    
    # starts with
    def startWith(self, prefix):
        node =self.root
        for c in prefix:
            if c not in node.children:
                return False
        node = node.children
        return True

# execution

trie = Trie()
print(trie.insert("vedant"))
print(trie.search("vedant"))
print(trie.search("dave"))
print(trie.root.word)
