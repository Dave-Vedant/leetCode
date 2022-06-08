def Node(val, negithbors):
    val = val
    neighbors = []

def cloneGraph(node):
    oldToNew = {}
    def dfs(node):
        if node in oldToNew:
            return oldToNew[node]

        copy = Node(node.val)
        oldToNew[node] = copy

        for nei in node.neighbor:
            copy.neightbors.append(dfs(nei))
        return copy

    return dfs(node)
        




