def Node(val, negithbors):
    val = val
    neighbors = []

def cloneGraph(node):

    def dfs(node):
        oldToNew = {}
        if node in oldToNew:
            return oldToNew[node]

        copy = Node(node.val)
        oldToNew[node] = copy

        for nei in node.neighbor:
            copy.neightbors.append(dfs(nei))
        return copy

    return dfs(node)
        

# Need to understand properly, can not understand the questions, why we need it in real life




