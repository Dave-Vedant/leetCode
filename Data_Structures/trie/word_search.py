# word search I (find horizontally or vertically)

def exist(board, word):
    ROWS, COLS = len(board), len(board[0])
    path = set()  # so we can not visit same character again...

    def dfs(r,c, i):
        if i == len(word):
            return True
        
        if (r<0 or c<0 or r>=ROWS or 
        c>=COLS or word[i]!= board[r][c] 
        or (r,c) in path):
            return False
        
        path.add((r,c))

        res = (dfs(r+1, c, i+1) or
        dfs(r-1, c, i+1) or
        dfs(r, c+1, i+1) or
        dfs(r, c-1, i+1))
        path.remove((r,c))
        return res

    # brute force..
    for r in range(ROWS):
        for c in range(COLS):
            if dfs(r,c,0):
                return True
    return False

        # time complexity = (M * N * 4^n)  
                  # n is lengh of word, each character have worst(max) 4 neighbour.
        # space complexity = O(n) -- length of work (as the set use the max path upto word length)



# in any direction, until character is connected as neighbour
# prefix tree (trie)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur= cur.children[c]
        cur.isWord = True

class Solution:
    def findWords(self, board, words):
        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board, len(board[0]))
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if (r<0 or c<0 or r== ROWS or c== COLS or (r,c) in visit or board[r][c] not in node.children or (r,c) in visit):
                return 
        
            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)

            dfs(r-1, c, node, word)
            dfs(r+1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)
      
            visit.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c, root, "")
    
        return list(res)
