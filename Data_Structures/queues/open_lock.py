from collections import deque

# bfs
def openLock(deadends, target):

    if "0000" in deadends:
        return -1

    # helper
    def children(lock):
        res = []
        for i in range(4):
            digit = str((int(lock[i]) +1) % 10)
            res.append(lock[:i] + digit + lock[i+1:])

            digit = str((int(lock[i]) -1+ 10) % 10)
            res.append(lock[:i] + digit + lock[i+1:])
        return res


    q = deque()
    q.append(["0000", 0]) # [lock, turns]
    visited = set()

    while q:
        lock, turns = q.popleft()           # if q.pop() its work as dfs...
        if lock == target:
            return turns
        
        for child in children(lock):
            if child not in visited:
                visited.add(child)
                q.append([child, turns +1])

    return -1