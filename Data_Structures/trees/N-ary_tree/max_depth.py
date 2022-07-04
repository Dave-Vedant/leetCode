def maxDepth(root):
    stack = []
    if root is not None:
        stack.append((1,root))

    depth = 0
    while stack != []:
        current_depth, root = stack.pop()
        if root is not None:
            depth = max(depth, current_depth)
            for c in root.children:
                stack.append((current_depth+1, c))
    return depth